# Functional Specification Document

## Overview
The MMsuit Application is a Python-based GUI tool designed to aid wet-lab researchers, biophysicists, biochemists, and educators study enzyme kinetics using the Michaelis-Menten equation. This tool will be a companion application for conducting enzyme experiments and simulations, providing real-time graphical analysis of various kinetics-related parameters. The application includes two primary functions:

1. **inputexperiment()**: The user uploads experimental data (substrate concentration, enzyme concentration, and corresponding reaction rates). The application processes the data and calculates key enzyme kinetic parameters including $K_m$, $V_{max}$, $k_{cat}$, and $t_{1/2}$.
   
2. **experimentsimulator()**: The user inputs kinetic parameters like $K_m$, $V_{max}$, etc., and the application simulates enzyme kinetics and generates graphs, including the Michaelis-Menten curve, Lineweaver-Burk plot, and Eadie-Hofstee plot.

## 1. Application Features

### 1.1 **User Interface (UI) Overview**
The GUI will be intuitive, with drag-menu functionality for uploading data files and input fields for manually entering kinetic parameters. The UI will contain:

- **File Upload Interface**: Allows users to upload Excel or CSV files containing experimental data.
- **Data Input Fields**: Users can manually input values for various kinetic parameters (e.g., substrate concentration, enzyme concentration, reaction rates, $K_m$, $V_{max}$, etc.).
- **Results Output**: Displays computed results such as $K_m$, $V_{max}$, $k_{cat}$, and $t_{1/2}$.
- **Plotting Area**: Provides dynamic plots (Michaelis-Menten curve, Lineweaver-Burk plot, Eadie-Hofstee plot) based on the input or simulated data.

### 1.2 **Core Functionality**

#### 1.2.1 **Input Experiment Functionality:**
- **User Uploads Data**:
    - Supported file formats: CSV, XLSX (Excel).
    - The file must include columns for substrate concentration, enzyme concentration, and corresponding reaction response (i.e. fluorescence absorbance, force, etc).
    - Once uploaded, the data will be parsed and displayed for review.
    
- **Calculating Enzyme Kinetics Parameters**:
    - **$K_m$ (Michaelis constant)**: This value indicates the substrate concentration at which the reaction velocity is half of $V_{max}$.
    - **$V_{max}$ (Maximum velocity)**: The asymptote of the reaction velocity as substrate concentration increases.
    - **$k_{cat}$ (Turnover number)**: Describes the number of substrate molecules converted to product per enzyme molecule per unit time.
    - **$t_{1/2}$ (Half-life)**: Represents the time required for half the initial substrate to be converted to product.
    
- **User Interface Flow**:
    - Upload the data file.
    - Input enzyme concentration (if not provided in the file).
    - Select which kinetic parameters to calculate from a dropdown menu.
    - Click on "Calculate" to obtain the kinetic parameters.
    - Display results below the input area and *present them as text or downloadable as an Excel/CSV summary*.

#### 1.2.2 **Experiment Simulator Functionality:**
- **User Inputs Known Parameters**:
    - Users can manually enter values for $K_m$, $V_{max}$, and optionally other parameters like enzyme concentration.
    
- **Simulate Data**:
    - The application will simulate reaction velocities at different substrate concentrations, based on the input kinetic parameters.
    - The simulation will then plot the following graphs:
        - **Michaelis-Menten Plot**: Substrate concentration vs. reaction velocity.
        - **Lineweaver-Burk Plot**: A double reciprocal plot of $\frac{1}{V}$ versus $\frac{1}{[S]}$.
        - **Eadie-Hofstee Plot**: A plot of $V$ vs. $\frac{V}{[S]}$, showing a linear relationship.
        
- **User Interface Flow**:
    - Input values for $K_m$, $V_{max}$, and other parameters.
    - Choose a substrate concentration range for the simulation.
    - Click "Simulate" to generate data points and plots.
    - Display the results as dynamic, interactive plots.
    
### 1.3 **Data Visualization**
The application will include interactive plots that allow users to zoom, pan, and hover over data points for more detailed information.

- **Michaelis-Menten Curve**:
    - Plot showing the relationship between substrate concentration and reaction velocity. This will be an asymptotic curve.
    
- **Lineweaver-Burk Plot**:
    - Double reciprocal plot showing the inverse relationship between reaction velocity and substrate concentration.
    
- **Eadie-Hofstee Plot**:
    - A linear plot of reaction velocity ($V$) vs. velocity divided by substrate concentration ($V/[S]$).

### 1.4 **Exporting Results**
- Users can export their experimental results, kinetic parameters, and simulation data to CSV or Excel formats for further analysis.
  
### 1.5 **Error Handling**
- **File Upload Errors**: Clear error messages if the file format is incorrect or if required columns are missing.
- **Invalid Input**: Error messages will guide users to provide valid data, such as positive numerical values for concentration and velocity.
- **Invalid Calculations**: If certain parameter calculations are not possible due to insufficient data, the application will notify users.
## 2. Use Cases

### **Use Case 1: Input Experiment**

| **Attribute**            | **Details**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **ID**                   | U1                                                                         |
| **Actor**                | User                                                                        |
| **Preconditions**        | Excel or CSV file containing substrate concentrations, enzyme concentration, and reaction velocities in terms of corresponding reaction response (i.e. fluorescence absorbance, force, etc). |
| **Trigger**              | User uploads the data file.                                                 |
| **Main Flow**            | 1. Upload file. <br> 2. Data is processed and displayed. <br> 3. User inputs enzyme concentration (if missing). <br> 4. App calculates kinetic parameters. <br> 5. Results displayed. |
| **Postconditions**       | Kinetic parameters $ K_m$, $V_{max}$, $k_{cat}$, $t_{1/2}$ are calculated and displayed. |
| **Alternative Flow**     | Invalid file format or missing columns will prompt an error message for corrections. |

---

### **Use Case 2: Experiment Simulator**

| **Attribute**            | **Details**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **ID**                   | U2                                                                         |
| **Actor**                | User                                                                        |
| **Preconditions**        | Known kinetic parameters (e.g., $K_m$, $V_{max}$) are available.    |
| **Trigger**              | User inputs kinetic parameters and selects simulation options.              |
| **Main Flow**            | 1. Input parameters. <br> 2. Simulate reaction velocities. <br> 3. Generate interactive plots (Michaelis-Menten, Lineweaver-Burk, Eadie-Hofstee). <br> 4. Display results. |
| **Postconditions**       | Interactive plots (Michaelis-Menten, Lineweaver-Burk, Eadie-Hofstee) are displayed. |
| **Alternative Flow**     | Invalid input (e.g., negative or non-numeric values) triggers an error message prompting valid data. |

---

### **Use Case 3: Experiment Simulation (Varying $K_m$ and $V_{max}$)**

| **Attribute**            | **Details**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **ID**                   | U3                                                                         |
| **Actor**                | User                                                                        |
| **Preconditions**        | Interest in exploring the effect of varying $K_m$ and $V_{max}$.    |
| **Trigger**              | User inputs different values for $K_m$ and $V_{max}$.               |
| **Main Flow**            | 1. Enter varying  $K_m$ and $V_{max}$. <br> 2. Simulate reaction velocities. <br> 3. Generate interactive plots. <br> 4. Display results. |
| **Postconditions**       | Simulated data and interactive plots are generated based on varying $K_m$ and $V_{max}$. |
| **Alternative Flow**     | Invalid input (e.g., unrealistic values) prompts the user to enter valid data. |

