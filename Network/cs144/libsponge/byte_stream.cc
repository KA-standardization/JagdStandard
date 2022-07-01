#include "byte_stream.hh"

// Dummy implementation of a flow-controlled in-memory byte stream.

// For Lab 0, please replace with a real implementation that passes the
// automated checks run by `make check_lab0`.

// You will need to add private members to the class declaration in `byte_stream.hh`

using namespace std;

ByteStream::ByteStream(const size_t capacity) { cap_ = capacity; }

size_t ByteStream::write(const string &data) {
    size_t write_length = data.size();
    size_t remain_length = remaining_capacity();
    size_t will_write_length = 0;
    if (write_length <= remain_length) {
        buf_ += data;
        will_write_length = write_length;
    } else {
        will_write_length = remain_length;
        buf_ += data.substr(0, will_write_length);
    }

    used_bytes_ += will_write_length;
    total_write_bytes_ += will_write_length;

    return will_write_length;
}

//! \param[in] len bytes will be copied from the output side of the buffer
string ByteStream::peek_output(const size_t len) const { return buf_.substr(0, len); }

//! \param[in] len bytes will be removed from the output side of the buffer
void ByteStream::pop_output(const size_t len) {
    total_read_bytes_ += len;
    buf_.erase(0, len);
    used_bytes_ -= len;
}

//! Read (i.e., copy and then pop) the next "len" bytes of the stream
//! \param[in] len bytes will be popped and returned
//! \returns a string
std::string ByteStream::read(const size_t len) {
    size_t will_read_length = 0;
    if (len <= used_bytes_) {
        will_read_length = len;
    } else {
        will_read_length = used_bytes_;
    }
    string str = peek_output(will_read_length);
    pop_output(will_read_length);
    return str;
}

void ByteStream::end_input() { is_EOF_ = true; }

bool ByteStream::input_ended() const { return is_EOF_; }

size_t ByteStream::buffer_size() const { return used_bytes_; }

bool ByteStream::buffer_empty() const { return used_bytes_ == 0; }

bool ByteStream::eof() const { return is_EOF_ && used_bytes_ == 0; }

size_t ByteStream::bytes_written() const { return total_write_bytes_; }

size_t ByteStream::bytes_read() const { return total_read_bytes_; }

size_t ByteStream::remaining_capacity() const { return cap_ - used_bytes_; }
