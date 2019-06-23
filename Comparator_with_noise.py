
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute

q1 = QuantumRegister(9)
c1 = ClassicalRegister(9)
qc1 = QuantumCircuit(q1, c1)



# qc1.x(q1[0])
qc1.x(q1[1])
#

# qc1.x(q1[5])

qc1.x(q1[6])



qc1.h(q1[1])
qc1.h(q1[6])

qc1.x(q1[1])
qc1.ccx(q1[0], q1[1], q1[2])
qc1.x(q1[0])
qc1.x(q1[1])
qc1.ccx(q1[0], q1[1], q1[3])
qc1.x(q1[0])

qc1.x(q1[6])
qc1.ccx(q1[5], q1[6], q1[7])
qc1.x(q1[5])
qc1.x(q1[6])
qc1.ccx(q1[5], q1[6], q1[8])
qc1.x(q1[5])

qc1.ccx(q1[2], q1[3], q1[4])
qc1.ccx(q1[7], q1[4], q1[2])
qc1.ccx(q1[8], q1[4], q1[3])



qc1.measure(q1[2], c1[2])
qc1.measure(q1[3], c1[3])

backend = Aer.get_backend('qasm_simulator')
job_sim = execute(qc1, backend)
sim_result = job_sim.result()


config = {
    'noise_params': {
        'relaxation_rate': 1/50,
        'thermal_populations': [0.99, 0.01],
        'CX': {'gate_time': 0.1},
        'U': {'gate_time': 0.01},
        'U': {'p_pauli': [0.01, 0, 0]}
    }
}
sim = 'local_qasm_simulator_cpp'
job = execute(qc1, sim, config)
result = job.result()
result.get_counts()



print(sim_result.get_counts(qc1))