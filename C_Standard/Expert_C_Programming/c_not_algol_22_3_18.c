//
// Created by root on 2022/3/18.
//
#define STRING char *
#define IF if(
#define THEN ){
#define ELSE }else(
#define FI ;}
#define WHILE while(
#define DO ){
#define OD ;}
#define INT int
#define BEGIN {
#define END }

INT foo1(s1, s2)
        STRING s1;
        STRING s2;
BEGIN
    WHILE*s1++ == *s2
    DO IF*s2++ == 0
        THEN return (0);FI OD
    return (*--s1 - *s2);
END

int bar2(s1, s2)char *s1, *s2;{
//int bar(char *s1,char *s2){
    while (*s1++ == *s2) {
        if (*s2++ == 0) return (0);
    }
    return (*--s1 - *s2);
}


