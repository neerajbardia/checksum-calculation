# checksum-calculation

Checksum is a value that can be used to verify the integrity of the message that is being transferred, mainly used in IPv4 address mode and also in cryptographic systems.

# Calculation
Checksum is calculated by adding the bits of the data, i.e. if the message is converted to binary as with all data. then all the values are added together, if carry is generated then it it added to the starting of the bits and the resulting value is the checksum of the data.

This code can be split into two and used in conjecture with socket programming, to form a more smooth undestanding.
