#ifndef GOLPI_BOARD_H
#define GOLPI_BOARD_H

#include <stdint.h>
#include <stdio.h>
#include <memory.h>

#define GOLPI_BORDER_MODE_TRANSPARENT 0
#define GOLPI_BORDER_MODE_SOLID 1
#define GOLPI_BORDER_MODE_OFFSET 2

typedef struct
{
    char* raw_data;

    uint32_t x_dim;
    uint32_t y_dim;

    int32_t border_mode;
} GolpiBoard;

GolpiBoard golpi_board_create(char* raw_data, uint32_t x_dim, uint32_t y_dim, int32_t border_mode)
{
    return (GolpiBoard){.raw_data = raw_data, .x_dim = x_dim, .y_dim = y_dim, .border_mode = border_mode};
}

char golpi_board_index(GolpiBoard* board, uint32_t x, uint32_t y)
{
    return board->raw_data[board->y_dim * y + x];
}

char* golpi_board_index_ref(GolpiBoard* board, uint32_t x, uint32_t y)
{
    return &(board->raw_data[board->y_dim * y + x]);
}

uint8_t golpi_board_check_zero(GolpiBoard* board)
{
    for(uint32_t i = 0; i < board->x_dim * board->y_dim; i++)
    {
        if(board->raw_data[i] == '*') return 0;
    }
    return 1;
}

uint8_t golpi_board_active_surrounding_cells(GolpiBoard* board, uint32_t cell_x, uint32_t cell_y)
{
    int32_t lcorner_x = cell_x - 1;
    int32_t lcorner_y = cell_y - 1;
    int32_t ucorner_y = cell_y + 1;
    int32_t ucorner_x = cell_x + 1;

    uint32_t surrounding_cells = 0;
    switch(board->border_mode)
    {
        case 0:
            if(lcorner_x < 0) {lcorner_x = board->x_dim - 1;}
            if(lcorner_y < 0) {lcorner_y = board->y_dim - 1;}
            if(ucorner_y >= board->y_dim) {ucorner_y = 0;}
            if(ucorner_x >= board->x_dim) {ucorner_x = 0;}

            surrounding_cells += (golpi_board_index(board, ucorner_x, ucorner_y) == '*');
            surrounding_cells += (golpi_board_index(board, lcorner_x, ucorner_y) == '*');
            surrounding_cells += (golpi_board_index(board, cell_x, ucorner_y) == '*');

            surrounding_cells += (golpi_board_index(board, ucorner_x, cell_y) == '*');
            surrounding_cells += (golpi_board_index(board, lcorner_x, cell_y) == '*');

            surrounding_cells += (golpi_board_index(board, ucorner_x, lcorner_y) == '*');
            surrounding_cells += (golpi_board_index(board, cell_x, lcorner_y) == '*');
            surrounding_cells += (golpi_board_index(board, lcorner_x, lcorner_y) == '*');
            break;
        case 1:
            break;
        case 2:
            break;
        default:
            break;
    }
    return surrounding_cells;
}

void golpi_board_simulate(GolpiBoard* board)
{
    char temp_board_dt[board->x_dim * board->y_dim];
    memcpy(temp_board_dt, board->raw_data, board->x_dim * board->y_dim);
    GolpiBoard temp_board = (GolpiBoard){.raw_data = temp_board_dt, .x_dim = board->x_dim, .y_dim = board->y_dim, .border_mode = board->border_mode};

    for(uint32_t j = 0; j < board->x_dim; j++)
    {
        for(uint32_t i = 0; i < board->y_dim; i++)
        {
            uint8_t surrounding_cells = golpi_board_active_surrounding_cells(board, i, j);
            if(golpi_board_index(board, i, j) == '*')
            {
                if((surrounding_cells < 2) || (surrounding_cells > 3)) *golpi_board_index_ref(&temp_board, i, j) = ' '; 
                continue;
            }
            if(surrounding_cells == 3) *golpi_board_index_ref(&temp_board, i, j) = '*';
        }
    }

    memcpy(board->raw_data, temp_board_dt, board->x_dim * board->y_dim);
}

void golpi_board_print(GolpiBoard* board)
{
    for(uint32_t j = 0; j < board->x_dim; j++)
    {
        for(uint32_t i = 0; i < board->y_dim; i++)
        {
            printf("%c", golpi_board_index(board, i, j));
        }
        printf("\n");
    }
    printf("\n\n");
}

#endif