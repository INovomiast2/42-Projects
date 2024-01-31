/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/24 10:48:37 by ivnovomi          #+#    #+#             */
/*   Updated: 2024/01/24 11:27:33 by ivnovomi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

char	*ft_free(char *buffer, char *bff)
{
	char	*temp;

	temp = ft_strjoin(buffer, bff);
	if (buffer)
	{
		free(buffer);
		buffer = NULL;
	}
	return (temp);
}

char	*ft_read_fd(int fd, char *res)
{
	char	*buff;
	int		r_byte;

	if (!res)
		res = ft_calloc(1, 1);
	if (!res)
		return (NULL);
	buff = ft_calloc(BUFFER_SIZE + 2, sizeof(char));
	if (!buff)
		return (NULL);
	r_byte = 1;
	while (r_byte > 0)
	{
		r_byte = read(fd, buff, BUFFER_SIZE);
		if (r_byte == -1)
		{
			free(buff);
			return (buff = NULL, NULL);
		}
		buff[r_byte] = '\0';
		res = ft_free(res, buff);
		if (ft_strchr(buff, '\n'))
			break ;
	}
	return (free(buff), res);
}

char	*ft_next_line(char *buff)
{
	int		y;
	int		x;
	char	*line;

	y = 0;
	while (buff[y] && buff[y] != '\n')
		y++;
	if (!buff[y])
	{
		free(buff);
		return (NULL);
	}
	line = ft_calloc((ft_strlen(buff) - y + 2), sizeof(char));
	if (!line)
	{
		free(buff);
		return (NULL);
	}
	y++;
	x = 0;
	while (buff[y])
		line[x++] = buff[y++];
	line[x] = '\0';
	free(buff);
	return (line);
}

char	*ft_current_line(char *buff)
{
	int		i;
	char	*line;

	i = 0;
	while (buff[i] && buff[i] != '\n')
		i++;
	line = (char *)ft_calloc(i + 2, sizeof(char));
	if (!line)
		return (NULL);
	i = 0;
	while (buff[i] && buff[i] != '\n')
	{
		line[i] = buff[i];
		i++;
	}
	if (buff[i] && buff[i] == '\n')
		line[i++] = '\n';
	line[i] = '\0';
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*buffer[FD_SETSIZE];
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0 || fd >= FD_SETSIZE)
		return (NULL);
	if (!buffer[fd])
		buffer[fd] = ft_calloc(1, 1);
	buffer[fd] = ft_read_fd(fd, buffer[fd]);
	if (!buffer[fd])
	{
		free(buffer[fd]);
		buffer[fd] = NULL;
		return (NULL);
	}
	line = ft_current_line(buffer[fd]);
	if (!line)
	{
		free(buffer[fd]);
		buffer[fd] = NULL;
		return (NULL);
	}
	buffer[fd] = ft_next_line(buffer[fd]);
	if (!buffer[fd])
		return (free(line), NULL);
	return (line);
}
