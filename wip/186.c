#include <stdio.h>
#define PM 

typedef unsigned int uint32;

typedef struct {
    uint32 pos;
    uint32 buf[55];
} buf_t; 

buf_t initialize() {
    buf_t buffer;

    long long v;

    for (long long i = 1; i <= 55; i++) {
        v = (100003 - 200003 * i + 300007 * i*i*i) % 1000000;
        if (v < 0) v += 1000000;

        buffer.buf[(uint32) (i-1)] = (uint32) v;
    }

    buffer.pos = 0;

    return buffer;
}

uint32 get_next(buf_t *buffer) {
    uint32 pos = buffer->pos;

    uint32 ret = buffer->buf[pos];

    uint32 term_24 = (pos - 24 + 55) % 55;

    uint32 v = ((uint32) (ret + buffer->buf[term_24])) % 1000000;

    buffer->buf[pos] = v;
    buffer->pos = (pos + 1) % 55;

    return ret;
}

int main(int argc, char **argv) {
    buf_t b = initialize();

    for (int i = 0; i < 55; i++) {
        printf("Buffer[%i] = %u\n", i, b.buf[i]);
    }


    for (int i = 0; i < 100; i++) {
        printf("%d: %u\n", i, get_next(&b));
    }

    return 0;
}
