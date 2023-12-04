/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/04 11:11:30 by ivnovomi          #+#    #+#             */
/*   Updated: 2023/12/04 12:23:25 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_free(char *buffer, char *bff)
{
	char	*temp;

	temp = ft_strjoin(buffer, bff);
	free(buffer);
	return (temp);
}

char	*get_next_line(int fd)
{
}
