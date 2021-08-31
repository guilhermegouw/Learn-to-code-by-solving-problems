from .slot_machine import slot_machine


def test_slot_machine_case_1():
    output = slot_machine(48, 3, 10, 4)
    assert output == 'Martha plays 66 times before going broke.'