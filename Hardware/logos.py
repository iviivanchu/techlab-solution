def wait_nfc():

    logo = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x07, 0xe0, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe3, 
    0xff, 0xff, 0xc7, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 0xf9, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xfc, 0xff, 0xff, 0xff, 0xff, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xf3, 0xff, 0xff, 0xff, 
    0xff, 0xcf, 0xff, 0xff, 0xff, 0xff, 0xef, 0xff, 0xff, 0xff, 0xff, 0xf7, 0xff, 0xff, 0xff, 0xff, 
    0x9f, 0xff, 0xff, 0xff, 0xff, 0xf9, 0xff, 0xff, 0xff, 0xff, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xfe, 
    0xff, 0xff, 0xff, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f, 0xff, 0xff, 0xfd, 0xff, 0xff, 
    0x3f, 0xff, 0xff, 0xff, 0xbf, 0xff, 0xff, 0xfb, 0xff, 0xff, 0x3f, 0xff, 0xff, 0xff, 0xdf, 0xff, 
    0xff, 0xf7, 0xff, 0xf3, 0x1f, 0xfe, 0x00, 0x7f, 0xef, 0xff, 0xff, 0xef, 0xff, 0xf3, 0x8f, 0xfc, 
    0x1c, 0x3f, 0xf7, 0xff, 0xff, 0xdf, 0xff, 0x31, 0xcf, 0xfd, 0xff, 0xbf, 0xfb, 0xff, 0xff, 0xbf, 
    0xff, 0x38, 0xc7, 0xfd, 0xff, 0xbf, 0xfd, 0xff, 0xff, 0xbf, 0xfb, 0x18, 0xc7, 0xfd, 0xff, 0xbf, 
    0xfd, 0xff, 0xff, 0x7f, 0xf1, 0x9c, 0xe7, 0xfd, 0xff, 0xbf, 0xfe, 0xff, 0xff, 0x7f, 0xf9, 0x9c, 
    0xe7, 0xfd, 0xff, 0xbf, 0xfe, 0xff, 0xfe, 0xff, 0xf9, 0x8c, 0x67, 0xfd, 0xff, 0xbf, 0xff, 0x7f, 
    0xfe, 0xff, 0xf9, 0x8c, 0x67, 0xfd, 0xff, 0xaf, 0xff, 0x7f, 0xff, 0xff, 0xf9, 0x8c, 0x67, 0xfd, 
    0xff, 0xa7, 0xff, 0xff, 0xfd, 0xff, 0xf9, 0x9c, 0xe7, 0xfd, 0xf9, 0xa3, 0xff, 0xbf, 0xfd, 0xff, 
    0xf1, 0x9c, 0xe7, 0xfd, 0xf1, 0xa1, 0xff, 0xbf, 0xfd, 0xff, 0xfb, 0x18, 0xc7, 0xfd, 0xf0, 0xa0, 
    0xff, 0xbf, 0xfd, 0xff, 0xff, 0x39, 0xcf, 0xfd, 0xf8, 0xa0, 0xff, 0xbf, 0xfd, 0xff, 0xff, 0x71, 
    0xcf, 0xfd, 0xf8, 0x20, 0x7f, 0xbf, 0xff, 0xff, 0xff, 0xf3, 0x8f, 0xfd, 0xf8, 0x60, 0x7f, 0xff, 
    0xff, 0xff, 0xff, 0xf3, 0x1f, 0xfd, 0xfc, 0x20, 0x7f, 0xff, 0xfd, 0xff, 0xff, 0xff, 0x3f, 0xfd, 
    0xfc, 0x00, 0x7f, 0xbf, 0xfd, 0xff, 0xff, 0xff, 0x3f, 0xfd, 0xfc, 0x00, 0x7f, 0xbf, 0xfd, 0xff, 
    0xff, 0xff, 0xff, 0xfd, 0xfe, 0x00, 0x3f, 0xbf, 0xfd, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x02, 0x00, 
    0x3f, 0xbf, 0xfd, 0xff, 0x9c, 0xc0, 0x70, 0x7c, 0x1a, 0x00, 0x3f, 0xbf, 0xff, 0xff, 0x9c, 0xc0, 
    0x62, 0x3e, 0x00, 0x00, 0x3f, 0xff, 0xfe, 0xff, 0x8c, 0xcf, 0xcf, 0x3f, 0xff, 0x00, 0x3f, 0x7f, 
    0xfe, 0xff, 0x84, 0xcf, 0xcf, 0xff, 0xff, 0x80, 0x3f, 0x7f, 0xff, 0x7f, 0xa4, 0xc0, 0xcf, 0xff, 
    0xff, 0x80, 0x3e, 0xff, 0xff, 0x7f, 0xb0, 0xcf, 0xcf, 0xff, 0xff, 0xc0, 0x1e, 0xff, 0xff, 0xbf, 
    0xb0, 0xcf, 0xcf, 0x3f, 0xff, 0xe0, 0x1d, 0xff, 0xff, 0xbf, 0xb8, 0xcf, 0xc6, 0x3f, 0xff, 0xc0, 
    0x0d, 0xff, 0xff, 0xdf, 0xbc, 0xcf, 0xe0, 0x7f, 0xff, 0xd0, 0x0b, 0xff, 0xff, 0xef, 0xff, 0xff, 
    0xf9, 0xff, 0xff, 0xc0, 0x37, 0xff, 0xff, 0xf7, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xef, 0xff, 
    0xff, 0xfb, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xdf, 0xff, 0xff, 0xfd, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xbf, 0xff, 0xff, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f, 0xff, 0xff, 0xff, 
    0x7f, 0xff, 0xff, 0xff, 0xff, 0xfe, 0xff, 0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 0xff, 0xff, 0xf9, 
    0xff, 0xff, 0xff, 0xff, 0xef, 0xff, 0xff, 0xff, 0xff, 0xf7, 0xff, 0xff, 0xff, 0xff, 0xf3, 0xff, 
    0xff, 0xff, 0xff, 0xcf, 0xff, 0xff, 0xff, 0xff, 0xfc, 0xff, 0xff, 0xff, 0xff, 0x3f, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 0xf9, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe3, 0xff, 0xff, 
    0xc7, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x07, 0xe0, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
    return logo
