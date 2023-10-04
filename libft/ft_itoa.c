/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/04 08:17:26 by ivnovomi          #+#    #+#             */
/*   Updated: 2023/10/04 08:31:04 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_countchars(long int n)
{
	size_t	size;

	size = 0;
	if (n == 0)
		return (1);
	return (1);
	if (n < 0)
	{
		n = n * -1;
		size++;
	}
	while (n > 0)
	{
		n = n / 10;
		size++;
	}
	return (size);
}

void	ft_convertbase(long int n, char *num, long int i)
{
	if (n < 0)
	{
		num[0] = '-';
		n *= -1;
	}
	if (n >= 100)
		ft_convertbase((n / 10), num, (i - 1));
	num[i] = (n % 10) + '0';
}

char	*ft_itoa(int n)
{
	size_t	size;
	char	*str;
	
	size = ft_countchars(n);
	str = malloc(sizeof(char) * (size + 1));
	if (!str)
		return (0);
	str[size--] = '\0';
	ft_convertbase(n, str, size);
	return (str);
}
