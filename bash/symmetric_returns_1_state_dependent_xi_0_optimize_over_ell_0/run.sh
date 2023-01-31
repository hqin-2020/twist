#!/bin/bash

#SBATCH --account=pi-lhansen
#SBATCH --job-name=run
#SBATCH --output=./job-outs/symmetric_returns_1_state_dependent_xi_0_optimize_over_ell_0/run.out
#SBATCH --error=./job-outs/symmetric_returns_1_state_dependent_xi_0_optimize_over_ell_0/run.err
#SBATCH --time=0-12:00:00
#SBATCH --partition=caslake
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load julia/1.7.3
srun julia newsets_twocapitals.jl  --symmetric_returns 1 --state_dependent_xi 0 --optimize_over_ell 0

