# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from uuid import uuid4

import pytest

from cript import *

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

generic_name = f"test_{uuid4()}"
generic_collection = f"col_{uuid4()}"
generic_experiment = f"exp_{uuid4()}"
generic_process = f"exp_{uuid4()}"
generic_material1 = f"mat_{uuid4()}"
generic_inventory = f"inventory_{uuid4()}"
generic_computation= f"computation_{uuid4()}"


generic_uuid = f"{uuid4()}"
CREATED_UUID = None

class TestCript:

    @pytest.fixture(scope='session', autouse=True)
    def test_reusable_project_create(self) -> None:
        node = Project(name=generic_name)
        global CREATED_UUID
        CREATED_UUID = node.get("uuid")
        assert node.get("uuid") is not None

    def test_update_node(self) -> None:
        note = "mens et manus"
        node = Project(name=generic_name, notes=note)
        assert node.get("notes") == note

    def test_method_find_by_uuid(self) -> None:
        node = Project(uuid=CREATED_UUID)
        assert node.get("name") == generic_name

    def test_create_project(self) -> None:
        node = Project(
            name=f"proj{uuid4()}",
            notes="my notes",
        )
        assert node.get("name") is not None
    
    def test_create_collection_exisiting_project(self) -> None:
        col1=Collection(name=generic_collection)
        proj = Project(uuid=CREATED_UUID, collection=[col1])
        assert col1.get("name") == generic_collection

    def test_create_experiment_exisiting_collection(self) -> None:
        exp1 = Experiment(name=generic_experiment)
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert exp1.get("name") == generic_experiment


    def test_create_material(self) -> None:
        comp_forcefield= ComputationalForcefield(key="mmff", building_block="atom")
        mat2 = Material(name=f"mat_{uuid4()}")
        proj1 = Project(uuid=CREATED_UUID, material=[mat2])
        mat1 = Material(
            name=generic_material1,
            bigsmiles="{[][<]CCO[>][]}",
            computational_forcefield=comp_forcefield,
            component=[mat2]
        )
        proj1 = Project(uuid=CREATED_UUID, material=[mat1])
        assert mat1.get("name") == generic_material1

    def test_create_material_property(self) -> None:
        prop1 = Property(key="air_flow", type="number", unit="L/s", value=1)
        mat1 = Material(name=generic_material1, property=[prop1])
        proj1 = Project(uuid=CREATED_UUID, material=[mat1])
        assert prop1.get("uuid") is not None


    def test_create_inventory(self) -> None:
        mat1 = Material(name=generic_material1)
        mat2 = Material(name=f"mat_{uuid4()}")
        inv1 = Inventory(name=generic_inventory, material=[mat1, mat2])
        col1 = Collection(name=generic_collection, inventory=[inv1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1], material=[mat1, mat2])
        assert inv1.get("uuid") is not None


    def test_create_computation(self) -> None:
        comp1 = Computation(name=generic_computation, type="MC")
        exp1 = Experiment(name=generic_experiment, computation=[comp1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert comp1.get("uuid") is not None


    def test_create_computation_software(self) -> None:
        soft1 = SoftwareConfiguration()
        comp1 = Computation(name=generic_computation, type="MC", software_configuration=[soft1])
        exp1 = Experiment(name=generic_experiment, computation=[comp1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert comp1.get("uuid") is not None


    def test_create_computation_process(self) ->None:
        file1 = File(type=f"logs", source="https://criptapp.org/file1.txt")
        input_data1 = Data(type="nmr_h1", file=[file1])
        file2=File(type=f"logs", source="https://criptapp.org/file2.txt")
        output_data1 = Data(type="nmr_h1", file=[file2])
        comp_process1 = ComputationProcess(name="compr1", type="reaction", input_data=[input_data1], output_data=[output_data1])

        exp1 = Experiment(name=generic_experiment, computation_process=[comp_process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert comp_process1.get("uuid") is not None


    def test_create_process(self) -> None:
        process1 = Process(name=generic_process, type="mix")
        exp1 = Experiment(name=generic_experiment, process=[process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert process1.get("name") == generic_process
        assert process1.get("uuid") is not None

    def test_create_ingredient(self) -> None:
        mat1 = Material(name=generic_material1)
        qnt1 = Quantity(key="mass", value=2, unit="kg")
        ingredient = Ingredient(material=mat1, quantity=[qnt1])
        process1 = Process(name=generic_process, type="mix")
        exp1 = Experiment(name=generic_experiment, process=[process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1], material=[mat1])
        assert process1.get("name") == generic_process
        assert process1.get("uuid") is not None

    def test_create_algorithm(self) -> None:
        algorithm1 = Algorithm(key="advanced_sampling", type="analysis")
        software1 = Software(name="Test", version="1.0")
        soft1 = SoftwareConfiguration(software=software1, algorithm=[algorithm1])
        comp1 = Computation(name=generic_computation, type="MC", software_configuration=[soft1])
        exp1 = Experiment(name=generic_experiment, computation=[comp1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert algorithm1.get("uuid") is not None

    def test_create_citation(self) -> None:
        ref1 = Reference(type="web_site", title="https://app.criptapp.org")
        cit1 = Citation(type="reference", reference=ref1)
        process1 = Process(name="process1", type="mix", citation=[cit1])
        exp1 = Experiment(name=generic_experiment, process=[process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert cit1.get("uuid") is not None

    def test_create_reference(self) -> None:
        ref1 = Reference(type="web_site", title="https://app.criptapp.org")
        cit1 = Citation(type="reference", reference=ref1)
        process1 = Process(name="process1", type="mix", citation=[cit1])
        exp1 = Experiment(name=generic_experiment, process=[process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert ref1.get("uuid") is not None

    def test_create_computational_forcefield(self) -> None:
        comp_forcefield= ComputationalForcefield(key="mmff", building_block="atom")
        mat1 = Material(
            name=f"mat_{uuid4()}",
            bigsmiles="{[][<]CCO[>][]}",
            computational_forcefield=comp_forcefield,
        )
        proj1 = Project(uuid=CREATED_UUID, material=[mat1])
        assert comp_forcefield.get("uuid") is not None

    def test_create_condition(self) -> None:
        cond1 = Condition(key="energy", type="type", value=1)
        process1 = Process(name="process1", type="mix", condition=[cond1])
        exp1 = Experiment(name=generic_experiment, process=[process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert cond1.get("uuid") is not None

    def test_create_data(self) ->None:
        file1 = File(type=f"logs", source="https://criptapp.org/file1.txt")
        data1 = Data(type="nmr_h1", file=[file1])

        exp1 = Experiment(name=generic_experiment, data=[data1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert data1.get("uuid") is not None

    def test_create_file(self) ->None:
        file1 = File(type=f"logs", source="https://criptapp.org/file1.txt")
        data1 = Data(type="nmr_h1", file=[file1])
        # TODO add test for s3
        exp1 = Experiment(name=generic_experiment, data=[data1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert file1.get("uuid") is not None

    def test_create_equipment(self) -> None:
        equip1 = Equipment(key="burner")
        process1 = Process(name="process1", type="mix", equipment=[equip1])
        exp1 = Experiment(name=generic_experiment, process=[process1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert equip1.get("uuid") is not None

    def test_create_parameter(self) -> None:
        param1 = Parameter(key="bond_type", value="1")
        algorithm1 = Algorithm(key="advanced_sampling", type="analysis", parameter=[param1])
        software1 = Software(name="Test", version="1.0")
        soft1 = SoftwareConfiguration(software=software1, algorithm=[algorithm1])
        comp1 = Computation(name=generic_computation, type="MC", software_configuration=[soft1])
        exp1 = Experiment(name=generic_experiment, computation=[comp1])
        col1 = Collection(name=generic_collection, experiment=[exp1])
        proj1 = Project(uuid=CREATED_UUID, collection=[col1])
        assert param1.get("uuid") is not None

    def test_delete_attribute(self) -> None:
        proj1 = Project(uuid=CREATED_UUID)
        proj1.delete(notes=None)
        assert not hasattr(proj1, 'notes')

    def test_unlink_child(self) -> None:
        mat1 = Material(name=f"mat_{uuid4()}")
        proj1 = Project(uuid=CREATED_UUID, material=[mat1])
        proj1.delete(material=[mat1])
        assert not any(mat1.get("uuid") == l.get("uuid") for l in proj1.material)

    def test_unlink_all_children(self) -> None:
        mat1 = Material(name=f"mat_{uuid4()}")
        proj1 = Project(uuid=CREATED_UUID, material=[mat1])
        proj1.delete(material=None)
        assert proj1.get("material") is None

    def test_delete_node(self) -> None:
        proj1 = Project(uuid=CREATED_UUID)
        proj1.delete()
        assert proj1.get("uuid") is None

    def test_delete_unitialized_node(self) -> None:
        col1 = Collection(name=generic_collection)
        with pytest.raises(ValueError):
            col1.delete()
