#ifndef BWA_H_INCLUDED
#define BWA_H_INCLUDED

#include <float.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define GAP -2.0
#define MATCH 4.0
#define MISMATCH -2.0

typedef enum { true, false } bool;

typedef struct {
 char *a;
 unsigned int alen;
 char *b;
 unsigned int blen;
} seq_pair;
typedef seq_pair *seq_pair_t;

typedef struct {
 double score;
 unsigned int prev[2];
} entry;
typedef entry *entry_t;

typedef struct {
 unsigned int m;
 unsigned int n;
 entry_t **mat;
} matrix;
typedef matrix *matrix_t;

static char* reverse(char *str);

static seq_pair_t traceback(seq_pair_t problem, matrix_t S, bool local);

static matrix_t create_matrix(unsigned int m, unsigned int n);

void destroy_matrix(matrix_t S);

void destroy_seq_pair(seq_pair_t pair);

static seq_pair_t smith_waterman(seq_pair_t problem, bool local);

#endif // BWA_H_INCLUDED
