/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/25 13:10:16 by ivnovomi          #+#    #+#             */
/*   Updated: 2024/03/26 12:31:15 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef UTILS_H
# define UTILS_H

#include <stdio.h>
#include "../libs/MLX42/include/MLX42/MLX42.h"
#include "../libs/libft/libft.h"
#include "fcntl.h"

# define TEXTURE_LOAD_FAILURE "TEXTURE LOADING FAILURE"

void    ft_throw_error(void);
mlx_image_t* loadImage(mlx_t* mlx, char *path);

#endif