#include "tcp_sender.hh"

#include "tcp_config.hh"

#include <random>

// Dummy implementation of a TCP sender

// For Lab 3, please replace with a real implementation that passes the
// automated checks run by `make check_lab3`.

using namespace std;

//! \param[in] capacity the capacity of the outgoing byte stream
//! \param[in] retx_timeout the initial amount of time to wait before retransmitting the oldest outstanding segment
//! \param[in] fixed_isn the Initial Sequence Number to use, if set (otherwise uses a random ISN)
TCPSender::TCPSender(const size_t capacity, const uint16_t retx_timeout, const std::optional<WrappingInt32> fixed_isn)
    : _isn(fixed_isn.value_or(WrappingInt32{random_device()()}))
    , _initial_retransmission_timeout{retx_timeout}
    , _stream(capacity) {
    retransmission_timeout_ = _initial_retransmission_timeout;
}

uint64_t TCPSender::bytes_in_flight() const { return bytes_in_flight_; }

void TCPSender::fill_window() {
    if (has_FIN_) {
        return;
    }

    TCPSegment tcpSegment;
    if (!has_SYN_) {
        tcpSegment.header().syn = true;
        send_tcp_segment(tcpSegment);
        has_SYN_ = true;
        return;
    }

    uint16_t tmp_window_size = window_size_ == 0 ? 1 : window_size_;
    // need send fin see zero-window as one-window
    if (_stream.eof() && (receive_ackno + tmp_window_size > _next_seqno)) {
        tcpSegment.header().fin = true;
        send_tcp_segment(tcpSegment);
        has_FIN_ = true;
        return;
    }

    while (!_stream.buffer_empty()) {
        if (_next_seqno > receive_ackno + tmp_window_size - 1) {
            break;
        }

        size_t max_length =
            min(static_cast<size_t>(receive_ackno + tmp_window_size - _next_seqno), _stream.buffer_size());
        max_length = min(max_length, TCPConfig::MAX_PAYLOAD_SIZE);
        if (max_length == 0) {
            break;
        }

        tcpSegment.payload() = _stream.read(max_length);
        // piggyback data in FIN
        if (_stream.eof() && tcpSegment.length_in_sequence_space() < tmp_window_size) {
            tcpSegment.header().fin = true;
            has_FIN_ = true;
        }
        send_tcp_segment(tcpSegment);
    }
}

//! \param ackno The remote receiver's ackno (acknowledgment number)
//! \param window_size The remote receiver's advertised window size
void TCPSender::ack_received(const WrappingInt32 ackno, const uint16_t window_size) {
    uint64_t abs_ack = unwrap(ackno, _isn, _next_seqno);

    //    if (abs_ack > _next_seqno || segments_wait_.empty()) {
    //        return;
    //    }
    if (abs_ack > _next_seqno) {
        return;
    }

    if (abs_ack >= receive_ackno) {
        receive_ackno = abs_ack;
        window_size_ = window_size;
    }

    while (!segments_wait_.empty()) {
        TCPSegment tcpSegment = segments_wait_.front();
        uint64_t first_seq = unwrap(tcpSegment.header().seqno, _isn, _next_seqno);
        if (abs_ack <= first_seq + tcpSegment.length_in_sequence_space() - 1) {
            return;
        }
        segments_wait_.pop();
        bytes_in_flight_ -= tcpSegment.length_in_sequence_space();

        retransmission_timeout_ = _initial_retransmission_timeout;
        consecutive_retransmissions_ = 0;
        pass_time_ = 0;
    }

    if (segments_wait_.empty()) {
        timer_running_ = false;
    } else {
        timer_running_ = true;
    }
}

//! \param[in] ms_since_last_tick the number of milliseconds since the last call to this method
void TCPSender::tick(const size_t ms_since_last_tick) {
    if (!timer_running_) {
        return;
    }

    pass_time_ += ms_since_last_tick;
    if (pass_time_ >= retransmission_timeout_ && !segments_wait_.empty()) {
        TCPSegment tcpSegment = segments_wait_.front();
        _segments_out.push(tcpSegment);
        pass_time_ = 0;

        // syn packet need x2
        if (window_size_ > 0 || tcpSegment.header().syn) {
            consecutive_retransmissions_++;
            retransmission_timeout_ *= 2;
        }
    }
}

unsigned int TCPSender::consecutive_retransmissions() const { return consecutive_retransmissions_; }

void TCPSender::send_empty_segment() {
    TCPSegment seg;
    seg.header().seqno = wrap(_next_seqno, _isn);
    if (stream_in().error()) {
        seg.header().rst = true;
    }
    _segments_out.push(seg);
}

void TCPSender::send_tcp_segment(TCPSegment &tcpSegment) {
    tcpSegment.header().seqno = wrap(_next_seqno, _isn);
    _next_seqno += tcpSegment.length_in_sequence_space();
    _segments_out.push(tcpSegment);
    segments_wait_.push(tcpSegment);
    bytes_in_flight_ += tcpSegment.length_in_sequence_space();
    if (!timer_running_) {
        timer_running_ = true;
        pass_time_ = 0;
    }
}
