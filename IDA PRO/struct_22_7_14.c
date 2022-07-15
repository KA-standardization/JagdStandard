struct ch8_struct {
    int field1;
    short field2;
    char field3;
    int field4;
    double field5;
};
struct ch8_struct g_struct;

int main() {
//    struct ch8_struct c8 = {
//            10,
//            1,
//            'a',
//            20,
//            30.1
//    };

    g_struct.field1 = 10;
    g_struct.field2 = 20;
    g_struct.field3 = 30;
    g_struct.field4 = 40;
    g_struct.field5 = 50.0;


    return 0;
}