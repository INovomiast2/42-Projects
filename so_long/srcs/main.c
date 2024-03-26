/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/25 13:05:34 by ivnovomi          #+#    #+#             */
/*   Updated: 2024/03/26 12:30:26 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/so_long.h"

int32_t	main(int ac, char **av) {
	t_game game;
	game.mlx = mlx_init(WINDOW_WIDTH, WINDOW_HEIGHT, "SoLong - V.1.0.0", true);
	
	if (ac == 2 && ft_substr(av[1], '.', 0)) 
	{
		if (!game.mlx)
			ft_throw_error();
		
		mlx_image_t* img = mlx_new_image(game.mlx, 256, 256);
		if (!img || (mlx_image_to_window(game.mlx, img, 0, 0) < 0))
			ft_throw_error();

		mlx_put_pixel(img, 0, 0, 0xFF0000FF);
		
		game.player = loadImage(game.mlx, "assets/character/so_long_walk_sprite.png");

		ft_printf("Player Width: %d \n Player Height: %d", game.player->width, game.player->height);
		
		mlx_loop_hook(game.mlx, ft_move, &game);
		mlx_loop(game.mlx);
		mlx_terminate(game.mlx);
		return (EXIT_SUCCESS);
	}
	else
	{
		ft_printf("\033[0;31m[ERROR]:\033[0m No .ber file was passed thru params!");
		return (EXIT_FAILURE);
	}
	
	return (0);
}
