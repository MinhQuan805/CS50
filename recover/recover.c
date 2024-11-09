#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover argv[]\n");
        return 1;
    }
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Could not open\n");
        return 2;
    }
    unsigned char *buffer = malloc(512 * sizeof(BYTE));
    int j = 0;
    char filename[50];
    FILE *img = NULL;
    bool found = false;
    while (fread(buffer, sizeof(BYTE), 512, infile) != 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (found == true)
            {
                fclose(img);
            }
            else
            {
                found = true;
            }
            sprintf(filename, "%03i.jpg", j);
            img = fopen(filename, "w");
            fwrite(buffer, sizeof(BYTE), 512, img);
            j++;
        }
        // check if image already found
        else if (found == true)
        {
            fwrite(buffer, sizeof(BYTE), 512, img);
        }
    }
    free(buffer);
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(infile);
}
