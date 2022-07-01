#include "stream_reassembler.hh"

#include <iostream>

// Dummy implementation of a stream reassembler.

// For Lab 1, please replace with a real implementation that passes the
// automated checks run by `make check_lab1`.

// You will need to add private members to the class declaration in `stream_reassembler.hh`

using namespace std;

StreamReassembler::StreamReassembler(const size_t capacity)
    : _output(capacity), _capacity(capacity), buf_(capacity, '\0'), bitmap_(capacity, false) {}

//! \details This function accepts a substring (aka a segment) of bytes,
//! possibly out-of-order, from the logical stream, and assembles any newly
//! contiguous substrings and writes them into the output stream in order.
void StreamReassembler::push_substring(const string &data, const size_t index, const bool eof) {
    if (index >= next_index_ + _output.remaining_capacity()) {
        return;
    }

    if (index + data.size() <= next_index_) {
        if (eof) {
            is_eof_ = true;
        }
    } else {
        if (index + data.size() <= next_index_ + _output.remaining_capacity()) {
            if (eof) {
                is_eof_ = true;
            }
        }

        for (size_t i = index; i < next_index_ + _output.remaining_capacity() && i < index + data.size(); i++) {
            if (i >= next_index_ && !bitmap_[i - next_index_]) {
                buf_[i - next_index_] = data[i - index];
                bitmap_[i - next_index_] = true;
                unassembled_bytes_++;
            }
        }

        string str;
        while (bitmap_.front()) {
            str += buf_.front();
            buf_.pop_front();
            buf_.push_back('\0');
            bitmap_.pop_front();
            bitmap_.push_back(false);
        }

        size_t len = str.size();
        if (len > 0) {
            unassembled_bytes_ -= len;
            next_index_ += len;
            _output.write(str);
        }
    }

    if (is_eof_ && empty()) {
        _output.end_input();
    }
}

bool StreamReassembler::empty() const { return unassembled_bytes() == 0; }
size_t StreamReassembler::unassembled_bytes() const { return unassembled_bytes_; }
