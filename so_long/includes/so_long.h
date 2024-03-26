/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/25 13:05:44 by ivnovomi          #+#    #+#             */
/*   Updated: 2024/03/26 12:30:19 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

#include "../libs/MLX42/include/MLX42/MLX42.h"
#include "../libs/libft/libft.h"
#include <math.h>
#include <fcntl.h>
#include "maps.h"
#include "utils.h"
#include "hooks.h"

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600

typedef struct s_game
{
    mlx_t* mlx;
    mlx_image_t* player;
    int player_x;
    int player_y;
    int moves;
    
}   t_game;


#endif