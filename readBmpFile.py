import struct
import os

def read_bmp_info(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    with open(file_path, "rb") as bmp:
        magic = bmp.read(2).decode("ascii", errors="ignore")

        if magic != "BM":
            print("File isnt BMP")
            return

        file_size = struct.unpack("<I", bmp.read(4))[0]

        bmp.seek(10)
        data_offset = struct.unpack("<I", bmp.read(4))[0]

        dib_header_size = struct.unpack("<I", bmp.read(4))[0]

        width = struct.unpack("<i", bmp.read(4))[0]
        height = struct.unpack("<i", bmp.read(4))[0]

        bmp.seek(28)
        bits_per_pixel = struct.unpack("<H", bmp.read(2))[0]

        print(f"Format: {magic}")
        print(f"Width: {width}")
        print(f"Height: {height}")
        print(f"Bits per pixel: {bits_per_pixel}")

def main():
    base_path = os.path.expanduser("~/Documents/git/digtal-image-processing/assets")
    file_path = os.path.join(base_path, "snail.bmp")

    read_bmp_info(file_path)

    return

if __name__ == "__main__":
    main()
        
