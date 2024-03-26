/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/25 13:12:46 by ivnovomi          #+#    #+#             */
/*   Updated: 2024/03/26 12:31:53 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/utils.h"

void    ft_throw_error(void)
{
    fprintf(stderr, "\033[31m[ERROR]:\033[0m %s", mlx_strerror(mlx_errno));
    exit(EXIT_FAILURE);
}

mlx_image_t* loadImage(mlx_t* mlx, char *path)
{
	mlx_texture_t* texture = mlx_load_png(path);
	if (texture == NULL)
	{
        free(texture);
		ft_throw_error();
	}

	mlx_image_t* image = mlx_texture_to_image(mlx, texture);
	if (image == NULL)
	{
        free(image);
		ft_throw_error();
	}

	if (mlx_image_to_window(mlx, image, 0, 0) != 0)
	{
		ft_throw_error();
	}

	return (image);
}
