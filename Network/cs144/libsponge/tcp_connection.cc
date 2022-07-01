#include "tcp_connection.hh"

#include <iostream>

// Dummy implementation of a TCP connection

// For Lab 4, please replace with a real implementation that passes the
// automated checks run by `make check`.

template <typename... Targs>
void DUMMY_CODE(Targs &&... /* unused */) {}

using namespace std;

size_t TCPConnection::remaining_outbound_capacity() const { return _sender.stream_in().remaining_capacity(); }

size_t TCPConnection::bytes_in_flight() const { return _sender.bytes_in_flight(); }

size_t TCPConnection::unassembled_bytes() const { return _receiver.unassembled_bytes(); }

size_t TCPConnection::time_since_last_segment_received() const { return time_since_last_segment_received_; }

void TCPConnection::segment_received(const TCPSegment &seg) {
    if (!is_active_) {
        return;
    }

    time_since_last_segment_received_ = 0;

    if (seg.header().rst) {
        immediate_shutdown(false);
        return;
    }

    // closed
    if (_sender.next_seqno_absolute() == 0) {
        // passive open
        if (seg.header().syn) {
            // todo Don't have ack no, so sender don't need ack
            _receiver.segment_received(seg);
            connect();
            log_print("closed -> syn-rcvd");
        }
        return;
    }

    // syn-sent
    if (_sender.next_seqno_absolute() == _sender.bytes_in_flight() && !_receiver.ackno().has_value()) {
        if (seg.header().syn && seg.header().ack) {
            // active open
            _sender.ack_received(seg.header().ackno, seg.header().win);
            _receiver.segment_received(seg);
            // send ack
            _sender.send_empty_segment();
            send_internet();
            // become established
            log_print("syn-sent -> established");
        } else if (seg.header().syn && !seg.header().ack) {
            // simultaneous open
            _receiver.segment_received(seg);
            // already send syn, need a ack
            _sender.send_empty_segment();
            send_internet();
            // become syn_rcvd
            log_print("syn-sent -> syn_rcvd");
        }
        return;
    }

    // syn-rcvd
    if (_receiver.ackno().has_value() && !_receiver.stream_out().input_ended() &&
        _sender.next_seqno_absolute() == _sender.bytes_in_flight()) {
        // receive ack
        // todo need ack
        _receiver.segment_received(seg);
        _sender.ack_received(seg.header().ackno, seg.header().win);
        log_print("syn-rcvd -> established");
        return;
    }

    // established, aka stream ongoing
    if (_sender.next_seqno_absolute() > _sender.bytes_in_flight() && !_sender.stream_in().eof()) {
        _sender.ack_received(seg.header().ackno, seg.header().win);
        _receiver.segment_received(seg);
        if (seg.length_in_sequence_space() > 0) {
            _sender.send_empty_segment();
        }
        _sender.fill_window();
        send_internet();
        if (seg.header().fin) {
            log_print("established -> close wait");
        }
        return;
    }

    // close wait
    if (!_sender.stream_in().eof() && _receiver.stream_out().input_ended()) {
        _sender.ack_received(seg.header().ackno, seg.header().win);
        _receiver.segment_received(seg);
        // try to send remain data
        _sender.fill_window();
        send_internet();
        log_print("close wait -> (send remain data) or (last ack)");
        return;
    }

    // FIN_WAIT_1
    if (_sender.stream_in().eof() && _sender.next_seqno_absolute() == _sender.stream_in().bytes_written() + 2 &&
        _sender.bytes_in_flight() > 0 && !_receiver.stream_out().input_ended()) {
        if (seg.header().fin && seg.header().ack) {
            _sender.ack_received(seg.header().ackno, seg.header().win);
            _receiver.segment_received(seg);
            _sender.send_empty_segment();
            send_internet();
            log_print("fin_wait_1 -> time_wait");
        } else if (seg.header().fin && !seg.header().ack) {
            _sender.ack_received(seg.header().ackno, seg.header().win);
            _receiver.segment_received(seg);
            _sender.send_empty_segment();
            send_internet();
            log_print("fin_wait_1 -> closing");
        } else if (!seg.header().fin && seg.header().ack) {
            _sender.ack_received(seg.header().ackno, seg.header().win);
            _receiver.segment_received(seg);
            send_internet();
            log_print("fin_wait_1 -> fin_wait_2");
        }

        return;
    }

    // CLOSING
    if (_sender.stream_in().eof() && _sender.next_seqno_absolute() == _sender.stream_in().bytes_written() + 2 &&
        _sender.bytes_in_flight() > 0 && _receiver.stream_out().input_ended()) {
        _sender.ack_received(seg.header().ackno, seg.header().win);
        _receiver.segment_received(seg);
        send_internet();
        log_print("closing -> time_wait");
        return;
    }

    // FIN_WAIT_2
    if (_sender.stream_in().eof() && _sender.next_seqno_absolute() == _sender.stream_in().bytes_written() + 2 &&
        _sender.bytes_in_flight() == 0 && !_receiver.stream_out().input_ended()) {
        _sender.ack_received(seg.header().ackno, seg.header().win);
        _receiver.segment_received(seg);
        _sender.send_empty_segment();
        send_internet();
        log_print("fin_wait_2 -> time_wait");
        return;
    }

    // TIME_WAIT
    if (_sender.stream_in().eof() && _sender.next_seqno_absolute() == _sender.stream_in().bytes_written() + 2 &&
        _sender.bytes_in_flight() == 0 && _receiver.stream_out().input_ended()) {
        if (seg.header().fin) {
            _sender.ack_received(seg.header().ackno, seg.header().win);
            _receiver.segment_received(seg);
            _sender.send_empty_segment();
            send_internet();
            log_print("time_wait -> time_wait (Still reply FIN)");
        }

        return;
    }

    _sender.ack_received(seg.header().ackno, seg.header().win);
    _receiver.segment_received(seg);
    _sender.fill_window();
    send_internet();
    log_print("not happen-----");
    log_print(to_string(_sender.stream_in().input_ended()));
    log_print(to_string(_sender.stream_in().eof()));
    log_print(to_string(_receiver.stream_out().input_ended()));
    log_print(to_string(_receiver.stream_out().eof()));
    log_print(to_string(_sender.bytes_in_flight()));
    log_print("not happen-----");
}

bool TCPConnection::active() const { return is_active_; }

size_t TCPConnection::write(const string &data) {
    if (!is_active_) {
        return 0;
    }
    if (data.empty()) {
        return 0;
    }

    size_t size = _sender.stream_in().write(data);
    _sender.fill_window();
    send_internet();
    return size;
}

//! \param[in] ms_since_last_tick number of milliseconds since the last call to this method
void TCPConnection::tick(const size_t ms_since_last_tick) {
    if (!is_active_) {
        return;
    }

    time_since_last_segment_received_ += ms_since_last_tick;
    _sender.tick(ms_since_last_tick);
    if (_sender.consecutive_retransmissions() > TCPConfig::MAX_RETX_ATTEMPTS) {
        log_print("Do immediate shutdown");
        immediate_shutdown(true);
        return;
    }
    send_internet();
}

void TCPConnection::end_input_stream() {
    _sender.stream_in().end_input();
    _sender.fill_window();
    send_internet();
    log_print("established or syn_rcvd -> fin_wait_1");
}

void TCPConnection::connect() {
    if (!is_active_) {
        return;
    }
    //    if (tcp_state_ != TCPState::State::LISTEN) {
    //        return;
    //    }
    _sender.fill_window();
    //    tcp_state_ = TCPState::State::SYN_SENT;
    send_internet();
}

void TCPConnection::send_internet() {
    while (!_sender.segments_out().empty()) {
        TCPSegment seg = _sender.segments_out().front();
        _sender.segments_out().pop();
        if (_receiver.ackno().has_value()) {
            seg.header().ack = true;
            seg.header().ackno = _receiver.ackno().value();
            seg.header().win = _receiver.window_size();
        }
        _segments_out.push(seg);
    }
    clean_shutdown();
}

void TCPConnection::immediate_shutdown(bool need_send) {
    _receiver.stream_out().set_error();
    _sender.stream_in().set_error();
    is_active_ = false;
    if (need_send) {
        TCPSegment seg;
        seg.header().rst = true;
        seg.header().win = _receiver.window_size();
        segments_out().push(seg);
    }
}

void TCPConnection::clean_shutdown() {
    if (_receiver.stream_out().input_ended() && !_sender.stream_in().eof()) {
        // passive close
        if (_linger_after_streams_finish) {
            log_print("linger become false, passive close");
        }
        _linger_after_streams_finish = false;
    }

    if (_receiver.stream_out().input_ended() && _sender.stream_in().eof() && _sender.bytes_in_flight() == 0) {
        if (!_linger_after_streams_finish || time_since_last_segment_received() >= 10 * _cfg.rt_timeout) {
            is_active_ = false;
        }
    }
}

void TCPConnection::log_print(const std::string &s) {
    //    std::cout<<s<<std::endl;
    if (false) {
        cerr << s << std::endl;
    }
    //    cerr << s << std::endl;
}

TCPConnection::~TCPConnection() {
    try {
        if (active()) {
            cerr << "Warning: Unclean shutdown of TCPConnection\n";

            // Your code here: need to send a RST segment to the peer
        }
    } catch (const exception &e) {
        std::cerr << "Exception destructing TCP FSM: " << e.what() << std::endl;
    }
}
