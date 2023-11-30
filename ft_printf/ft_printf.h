/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/11 14:34:20 by ivnovomi          #+#    #+#             */
/*   Updated: 2023/11/30 17:37:03 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <stdarg.h>
# include <unistd.h>

// Prints
int		ft_print_char(char c);
int		ft_print_str(char *str);
int		ft_print_dec(int nb);
int		ft_print_uns(unsigned int nb);
int		ft_print_hex(unsigned long long nb, char c);
int		ft_print_ptr(unsigned long long ptr);
// Printf
int		ft_printf(const char *format, ...);
// Utils
int		ft_countn(long long nb);
void	ft_putnbr(int nb);

#endif