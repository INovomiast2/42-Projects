/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   hooks.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/26 11:25:24 by ivnovomi          #+#    #+#             */
/*   Updated: 2024/03/26 12:04:29 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# include "../includes/hooks.h"

void    ft_move(void *param)
{
    t_game *game;

    game = (t_game *)param;
    if (!game || !game->mlx)
        ft_throw_error();
    
    if (mlx_is_key_down(game->mlx, MLX_KEY_ESCAPE))
        mlx_close_window(game->mlx);
    if (game->player && game->player->instances) {
        if (mlx_is_key_down(game->mlx, MLX_KEY_W) || mlx_is_key_down(game->mlx, MLX_KEY_UP))
            game->player->instances[0].y -= 5;
        if (mlx_is_key_down(game->mlx, MLX_KEY_S) || mlx_is_key_down(game->mlx, MLX_KEY_DOWN))
            game->player->instances[0].y += 5;
        if (mlx_is_key_down(game->mlx, MLX_KEY_A) || mlx_is_key_down(game->mlx, MLX_KEY_LEFT))
            game->player->instances[0].x -= 5;
        if (mlx_is_key_down(game->mlx, MLX_KEY_D) || mlx_is_key_down(game->mlx, MLX_KEY_RIGHT))
            game->player->instances[0].x += 5;
    }
}
