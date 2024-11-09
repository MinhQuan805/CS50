#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            average = round(average);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);

            int green = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);

            int blue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            image[i][j].rgbtRed = red;

            image[i][j].rgbtGreen = green;

            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int left = 0;
        int right = width - 1;
        while (left < right)
        {
            RGBTRIPLE temp = image[i][left];
            image[i][left] = image[i][right];
            image[i][right] = temp;
            left++;
            right--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int m = 0; m < height; m++)
    {
        for (int n = 0; n < width; n++)
        {
            temp[m][n] = image[m][n];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int total_red = 0;
            int total_blue = 0;
            int total_green = 0;
            int count = 0;
            for (int m = j - 1; m < j + 2; m++)
            {
                if (0 <= m && m < width)
                {
                    for (int k = i - 1; k < i + 2; k++)
                    {
                        if (0 <= k  && k < height)
                        {
                            total_red += image[k][m].rgbtRed;
                            total_blue += image[k][m].rgbtBlue;
                            total_green += image[k][m].rgbtGreen;
                            count++;
                        }
                    }
                }
            }
            temp[i][j].rgbtRed = round((float) total_red/ count);
            temp[i][j].rgbtBlue = round((float) total_blue/ count);
            temp[i][j].rgbtGreen = round((float) total_green/ count);
        }
    }
    for (int o = 0; o < height; o++)
    {
        for (int s = 0; s < width; s++)
        {
            image[o][s] = temp[o][s];
        }
    }
}
