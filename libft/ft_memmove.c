/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/09/14 18:03:10 by ivnovomi          #+#    #+#             */
/*   Updated: 2023/09/14 18:10:46 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	*ft_memmove(void *dst, const void *src, size_t len)
{
	char	*dest;
	char	*srce;

	dest = (char *)dst;
	srce = (char *)src;
	if (dest < srce)
	{
		while (len--)
			*dest++ = *srce++;
	}
	else
	{
		dest += len;
		srce += len;
		while (len--)
			*--dest = *--srce;
	}
	return (dst);
}
