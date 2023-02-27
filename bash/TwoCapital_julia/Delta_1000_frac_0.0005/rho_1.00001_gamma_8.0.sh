#!/bin/bash

#SBATCH --account=pi-lhansen
#SBATCH --job-name=1000_0.0005
#SBATCH --output=./job-outs//TwoCapital_julia/Delta_1000_frac_0.0005/rho_1.00001_gamma_8.0.out
#SBATCH --error=./job-outs//TwoCapital_julia/Delta_1000_frac_0.0005/rho_1.00001_gamma_8.0.err
#SBATCH --time=0-12:00:00
#SBATCH --partition=caslake
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load julia/1.7.3
srun julia /home/hqin/twist/newsets_twocapitals_modif.jl  --Delta 1000 --fraction 0.0005 --gamma 8.0 --rho 1.00001 --dataname TwoCapital_julia_1000_frac_0.0005
