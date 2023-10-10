/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/07 16:54:55 by ivnovomi          #+#    #+#             */
/*   Updated: 2023/10/09 10:37:09 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include "libft/libft.h"
# include <stdarg.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

# if defined(__linux__)
#  define PTRNULL "(nil)"
# elif defined(__APPLE__)
#  define PTRNULL "0x0"
# endif

/*<----------FLAGS---------->*/
typedef struct s_flags
{
	int	spec;
	int	width;
	int	left;
	int	zero;
	int	star;
	int	precision;
	int	hash;
	int	space;
	int	plus;
}		t_flags;

t_flags	ft_flags_init(void);
t_flags	ft_flag_left(t_flags flags);
t_flags	ft_flag_digit(char c, t_flags flags);
t_flags	ft_flag_width(va_list args, t_flags flags);
int		ft_flag_precision(const char *str, int pos, va_list args,
			t_flags *flags);

/*<-----PRINTF----->*/
int		ft_printf(const char *format, ...);
int		ft_print_arg(char type, va_list args, t_flags flags);

/*<-----PRINTF SPECIFIERS----->*/
// Chars
int		ft_printf_char(char c, t_flags flags);
int		ft_printf_c(char c);
// Strings
int		ft_printf_str(const char *str, t_flags flags);
int		ft_printf_s(const char *str);
int		ft_printf_s_pre(const char *str, int precision);
int		ft_printf_sign_pre(int n, t_flags *flags);
// Integers, Doubles
int		ft_printf_int(int n, t_flags flags);
int		ft_printf_integer(char *nbstr, int n, t_flags flags);
int		ft_printf_i(char *nbstr, int n, t_flags flags);
// Unsigned Integer
int		ft_printf_


#endif