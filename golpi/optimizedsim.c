#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define BOARD_SIZE 10
#define BOARD_INDEX(mat, i, j) mat[BOARD_SIZE * i + j]

/*void generate_random_board(char* board)
{
    size_t j = 0;
    size_t i = 0;
    for(; j < BOARD_SIZE; j++)
    {
        i = 0;
        for(; i < BOARD_SIZE; i++)
        {
            int rnd = rand();
            if(rnd > INT32_MAX / 2)
            {
                BOARD_INDEX(board, i, j) = ' ';
                continue;
            }
            BOARD_INDEX(board, i, j) = '*';
        }
    }
}*/
uint8_t board_is_zero(char* board)
{
    size_t j = 0;
    size_t i = 0;
    for(; j < BOARD_SIZE; j++)
    {
        i = 0;
        for(; i < BOARD_SIZE; i++)
        {
            if(BOARD_INDEX(board, i, j) == '*')
            {
                return 0;
            }
        }
    }
    return 1;
}
uint8_t active_surrounding_cells(char* board, size_t cell_x, size_t cell_y)
{
    int32_t lcorner_x = cell_x - 1;
    int32_t lcorner_y = cell_y - 1;
    int32_t ucorner_y = cell_y + 1;
    int32_t ucorner_x = cell_x + 1;
    if(lcorner_x < 0) {lcorner_x = BOARD_SIZE - 1;}
    if(lcorner_y < 0) {lcorner_y = BOARD_SIZE - 1;}
    if(ucorner_y >= BOARD_SIZE) {ucorner_y = 0;}
    if(ucorner_x >= BOARD_SIZE) {ucorner_x = 0;}

    uint8_t c = 0;
    if(BOARD_INDEX(board, ucorner_x, ucorner_y) == '*') {c++;}
    if(BOARD_INDEX(board, lcorner_x, ucorner_y) == '*') {c++;}
    if(BOARD_INDEX(board, cell_x, ucorner_y) == '*') {c++;}

    if(BOARD_INDEX(board, ucorner_x, cell_y) == '*') {c++;}
    if(BOARD_INDEX(board, lcorner_x, cell_y) == '*') {c++;}

    if(BOARD_INDEX(board, ucorner_x, lcorner_y) == '*') {c++;}
    if(BOARD_INDEX(board, cell_x, lcorner_y) == '*') {c++;}
    if(BOARD_INDEX(board, lcorner_x, lcorner_y) == '*') {c++;}

    return c;
}
void update_board(char* board)
{
    char update_board[BOARD_SIZE * BOARD_SIZE];
    size_t j = 0;
    size_t i = 0;
    for(; j < BOARD_SIZE; j++)
    {
        i = 0;
        for(; i < BOARD_SIZE; i++)
        {
            uint8_t surrounding = active_surrounding_cells(board, j, i);
            if(BOARD_INDEX(board, i, j) == '*')
            {
                if((surrounding < 2) || (surrounding > 3)) {BOARD_INDEX(update_board, i, j) = -1; continue;}
                BOARD_INDEX(update_board, i, j) = 0;
                continue;
            }
            if(surrounding == 3) {BOARD_INDEX(update_board, i, j) = 1;}
            BOARD_INDEX(update_board, i, j) = 0;
        }
    }
    j = 0;
    i = 0;
    for(; j < BOARD_SIZE; j++)
    {
        i = 0;
        for(; i < BOARD_SIZE; i++)
        {
            if(BOARD_INDEX(update_board, i, j) == 1)
            {
                BOARD_INDEX(board, i, j) = '*';
                continue;
            }
            if(BOARD_INDEX(update_board, i, j) == -1)
            {
                BOARD_INDEX(board, i, j) = ' ';
            }
        }
    }
}
void print_board(char* board)
{
    size_t j = 0;
    size_t i = 0;
    for(; j < BOARD_SIZE; j++)
    {
        i = 0;
        for(; i < BOARD_SIZE; i++)
        {
            printf("%c", BOARD_INDEX(board, i, j));
        }
        printf("\n");
    }
    printf("\n\n");
}

int main(int argc, char** argv)
{
    uint64_t seed = 0;
    uint64_t generations = 1;

    /*printf("Geben Sie den Seed ihrer Simulation ein (oder 0 fuer eine zufaellige Simulation): ");
    scanf("%llu", &seed);
    srand(seed == 0 ? time(NULL) : seed);*/
    printf("Geben Sie die Anzahl der Generationen ein, fuer die die Simulation laufen soll: ");
    scanf("%llu", &generations);

    char game_board[BOARD_SIZE * BOARD_SIZE] = {
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', ' ',
    };
    //generate_random_board(game_board);
    print_board(game_board);

    size_t g = 0;
    for(; g < generations; g++)
    {
        update_board(game_board);
        print_board(game_board);
        if(board_is_zero(game_board))
        {
            return 0;
        }
    }
    return 0;
}