from qiskit import *
q = QuantumRegister(2)
c = ClassicalRegister(2)
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])

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
job = execute(circ, sim, config)
result = job.result()
result.get_counts()