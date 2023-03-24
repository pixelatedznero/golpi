#include "board.h"

int main(int argc, char** argv)
{
    uint64_t generations = 1;

    printf("Generations: ");
    scanf("%llu", &generations);

    char game_board[10 * 11] = {
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    };
    GolpiBoard board = golpi_board_create(game_board, 10, 11, 0);
    golpi_board_print(&board);

    size_t g = 0;
    for(; g < generations; g++)
    {
        golpi_board_simulate(&board);
        golpi_board_print(&board);
        if(golpi_board_check_zero(&board)) return 0;
    }
    return 0;
}