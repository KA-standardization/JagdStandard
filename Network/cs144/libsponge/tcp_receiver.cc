#include "tcp_receiver.hh"

// Dummy implementation of a TCP receiver

// For Lab 2, please replace with a real implementation that passes the
// automated checks run by `make check_lab2`.

template <typename... Targs>
void DUMMY_CODE(Targs &&... /* unused */) {}

using namespace std;

void TCPReceiver::segment_received(const TCPSegment &seg) {
    if (isn_ == nullopt && !seg.header().syn) {
        return;
    }

    if (seg.header().syn) {
        isn_ = seg.header().seqno;
    }

    checkpoint += seg.length_in_sequence_space();
    int64_t buffer_index = 0;
    if (seg.header().syn) {
        buffer_index = unwrap(seg.header().seqno + 1, isn_.value(), checkpoint);
    } else {
        buffer_index = unwrap(seg.header().seqno, isn_.value(), checkpoint);
    }
    buffer_index -= 1;
    if (buffer_index < 0) {
        return;
    }
    _reassembler.push_substring(seg.payload().copy(), buffer_index, seg.header().fin);
}

optional<WrappingInt32> TCPReceiver::ackno() const {
    if (isn_ == nullopt) {
        return nullopt;
    }

    uint64_t written = stream_out().bytes_written() + 1;
    if (stream_out().input_ended()) {
        written++;
    }
    return wrap(written, isn_.value());
}

size_t TCPReceiver::window_size() const { return stream_out().remaining_capacity(); }
