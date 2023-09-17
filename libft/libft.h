/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/09/12 16:28:27 by ivnovomi          #+#    #+#             */
/*   Updated: 2023/09/17 07:29:42 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <stdio.h>
# include <unistd.h>

// Checks if the passed value is an alphabetic character.
int		ft_isalpha(int c);

// Checks if the passed value is a numeric character.
int		ft_isdigit(int c);

// Checks if the passed value is alphanumeric.
int		ft_isalnum(int c);

// Checks if the passed value is a 7-bit ASCII character.
int		ft_isascii(int c);

// Checks if the passed character is printable.
int		ft_isprint(int c);

// Calculates the length of the string pointed to by str.
int		ft_strlen(const char *str);

// Fills the first n bytes of the memory area pointed to by str.
void	*ft_memset(void *str, int c, size_t n);

// Erases the data in the n bytes of the memory.
void	ft_bzero(void *str, size_t n);

// Copies n bytes from memory area src to memory area dst.
void	*ft_memcpy(void *dst, const void *src, size_t n);

// Copies len bytes from string src to string dst.
void	*ft_memmove(void *dst, const void *src, size_t len);

// Copies the string pointed to by src to the buffer pointed to by dst.
size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize);

#endif