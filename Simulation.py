# Main Memory (RAM)
RAM = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

# Page Table
PAGE_TABLE = {i: i for i in range(len(RAM))}

# TLB
TLB = {}
TLB_SIZE = 4  # Can Store 4 Entries

# Cache Memory
CACHE = {}
CACHE_SIZE = 4  # Can Store 4 Values

# READ FUNCTION
def read_virtual_address(virtual_address):
    print(f"\nReading virtual address: {virtual_address}")
    
    # TLB Check
    if virtual_address in TLB:
        physical_address = TLB[virtual_address]
        print(f"Virtual address {virtual_address} found in TLB.")
    else:
        print(f"Virtual address {virtual_address} not found in TLB.")
        print(f"Looking up Page Table...")
        # Page Table Check
        if virtual_address in PAGE_TABLE:
            physical_address = PAGE_TABLE[virtual_address]
            print(f"Virtual address {virtual_address} found in Page Table.")
            # Update TLB (FIFO Replacement If full)
            if len(TLB) >= TLB_SIZE:
                oldest = next(iter(TLB))
                del TLB[oldest]
            TLB[virtual_address] = physical_address
        else:
            print(f"Virtual address {virtual_address} not found in Page Table.")
            return None

    # Cache Memory Check
    if physical_address in CACHE:
        print(f"Data for physical address {physical_address} found in Cache Memory.")
        data = CACHE[physical_address]
    else:
        print(f"Data for physical address {physical_address} not found in Cache Memory.")
        print(f"Fetching RAM...")
        data = RAM[physical_address]
        # Update Cache Memory (FIFO replacement if full)
        if len(CACHE) >= CACHE_SIZE:
            oldest = next(iter(CACHE))
            del CACHE[oldest]
        CACHE[physical_address] = data
    
    print(f"Data for virtual address {virtual_address} is: {data}")
    return data

# EXAMPLE READS
if __name__ == "__main__":
    read_virtual_address(3)
    read_virtual_address(7)
    read_virtual_address(3)
    read_virtual_address(12)
    read_virtual_address(0)
    read_virtual_address(15)
    read_virtual_address(3)