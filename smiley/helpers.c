#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtRed == 0x00)
            {
                image[i][j].rgbtBlue = 0x23;
                image[i][j].rgbtGreen = 0xff;
                image[i][j].rgbtRed = 0x55;
            }
        }
    }  // Change all black pixels to a color of your choosing
}
