def validUTF8(data):
    # Helper function to check if a byte is a valid start byte
    # of a UTF-8 character
    def is_start_byte(byte):
        return (byte >> 7) == 0 or (byte >> 5) == 0b110 or (byte >> 4) == 0b1110 or (byte >> 3) == 0b11110

    # Helper function to check if a byte is a continuation byte
    def is_continuation_byte(byte):
        return (byte >> 6) == 0b10

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        byte = data[i]

        # Check if the byte is a valid start byte
        if not is_start_byte(byte):
            return False

        # Determine the number of bytes in the current UTF-8 character
        if (byte >> 7) == 0:
            length = 1
        elif (byte >> 5) == 0b110:
            length = 2
        elif (byte >> 4) == 0b1110:
            length = 3
        elif (byte >> 3) == 0b11110:
            length = 4
        else:
            return False

        # Check if there are enough bytes left in the data for the current character
        if i + length > len(data):
            return False

        # Check that the following bytes are continuation bytes
        for j in range(1, length):
            if not is_continuation_byte(data[i + j]):
                return False

        # Move to the next character
        i += length

    return True

# Test the method

# Valid UTF-8 encoding: [01000001]
data1 = [65]
# Valid UTF-8 encoding
data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# Invalid UTF-8 encoding
data3 = [229, 65, 127, 256]
