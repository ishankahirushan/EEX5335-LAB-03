# 🧵 Memory Management Simulation in Python

This guide presents the implementation of a **memory management simulator** using **Python**, executed on **Windows 11** using **Visual Studio Code**. The simulator demonstrates how virtual addresses are translated and accessed through a simple memory hierarchy.

---

## 🖥️ System Environment

- **OS**: Windows 11 Pro (Version 24H2)  
- **Python**: 3.13.5 (or latest installed)  
- **IDE/Code Editor**: Visual Studio Code (v1.101)  
- **Execution Environment**: Local Windows 11 terminal / VS Code terminal  

---

## 🎯 Objective

To simulate virtual memory address translation and access by:  
- Implementing a **Translation Lookaside Buffer (TLB)**  
- Implementing a **Page Table**  
- Implementing a **Cache Memory**  
- Demonstrating **data retrieval from RAM** based on virtual addresses  
- Observing how TLB and Cache are updated during access requests  

---

## 📂 Assumptions Made

- RAM has **16 slots** with preset read-only values.  
- The **Page Table** uses a direct 1-to-1 mapping of virtual to physical addresses.  
- The **TLB** can store up to 4 mappings and uses **FIFO replacement** when full.  
- The **Cache** stores up to 4 recently accessed RAM values and also uses **FIFO replacement** when full.  
- Virtual addresses are limited to the **valid range 0–15**.  
- Only **read operations** are implemented; no writing to memory.  

---

## ⚙️ Step 1: Python Setup on Windows 11

1. Install **Python** from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Open **VS Code** and install the Python extension.  
3. Verify Python installation in terminal:  
   ```bash
   python --version
   ```  
4. Create a new folder for the lab and open it in VS Code.  

---

## 🧾 Step 2: Write Python Program

1. **Create Python file**  

2. **Paste the Python code**

```python
# Main Memory (RAM)
RAM = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

# Page Table
PAGE_TABLE = {i: i for i in range(len(RAM))}

# TLB
TLB = {}
TLB_SIZE = 4  # Can store 4 entries

# Cache Memory
CACHE = {}
CACHE_SIZE = 4  # Can store 4 values

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
        if virtual_address in PAGE_TABLE:
            physical_address = PAGE_TABLE[virtual_address]
            print(f"Virtual address {virtual_address} found in Page Table.")
            if len(TLB) >= TLB_SIZE:
                oldest = next(iter(TLB))
                del TLB[oldest]
            TLB[virtual_address] = physical_address
        else:
            print(f"Virtual address {virtual_address} not found in Page Table.")
            return None

    # Cache Check
    if physical_address in CACHE:
        print(f"Data for physical address {physical_address} found in Cache Memory.")
        data = CACHE[physical_address]
    else:
        print(f"Data for physical address {physical_address} not found in Cache Memory.")
        print(f"Fetching RAM...")
        data = RAM[physical_address]
        if len(CACHE) >= CACHE_SIZE:
            oldest = next(iter(CACHE))
            del CACHE[oldest]
        CACHE[physical_address] = data
    
    print(f"Data for virtual address {virtual_address} is: {data}")
    return data

# Example Reads
if __name__ == "__main__":
    read_virtual_address(3)
    read_virtual_address(7)
    read_virtual_address(3)
    read_virtual_address(12)
    read_virtual_address(0)
    read_virtual_address(15)
    read_virtual_address(3)
```

3. **Save the file**.  

4. **Run the program**:  
   ```bash
   python MemorySimulator.py
   ```  

---

## 🧪 Output Example

```
Reading virtual address: 3
Virtual address 3 not found in TLB.
Looking up Page Table...
Virtual address 3 found in Page Table.
Data for physical address 3 not found in Cache Memory.
Fetching RAM...
Data for virtual address 3 is: 40
```

Subsequent accesses show the TLB and Cache being updated with new addresses and data values.

---

## 📁 Repository Structure

```
.
├── MemorySimulator.py
└── README.md
```

---

## 📚 Key Concepts Demonstrated

- Virtual address translation using TLB and Page Table.  
- Data retrieval through Cache and RAM.  
- FIFO replacement policy for TLB and Cache.  
- Step-by-step simulation of memory access requests.  

---

## 🔗 Repository Link

[GitHub - ishankahirushan/EEX5335-LAB-03](https://github.com/ishankahirushan/EEX5335-LAB-03)

---

## 📝 Notes

This project is for **educational purposes** as part of the Operating Systems course (EEX5335) at the Open University of Sri Lanka. It demonstrates a simplified memory management simulation and does **not represent real system memory behavior**.

