# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from uuid import uuid4

import pytest

import cript

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


generic_uuid = f"{uuid4()}"

class TestCript:

    @pytest.fixture(scope="session")
    def generic_name(self):
        return f"test_{uuid4()}"

    @pytest.fixture(scope="session")
    def generic_collection(self):
        return f"col_{uuid4()}"

    @pytest.fixture(scope="session")
    def generic_experiment(self):
        return f"exp_{uuid4()}"

    @pytest.fixture(scope="session")
    def generic_process(self):
        return f"exp_{uuid4()}"
    @pytest.fixture(scope="session")
    def generic_material1(self):
        return f"mat_{uuid4()}"
    @pytest.fixture(scope="session")
    def generic_inventory(self):
        return f"inventory_{uuid4()}"
    @pytest.fixture(scope="session")
    def generic_computation(self):
        return f"computation_{uuid4()}"

    @pytest.fixture(scope='session', autouse=True)
    def project_uuid(self, generic_name) -> None:
        node = cript.Project(name=generic_name)
        created_uuid = node.get("uuid")
        assert node.get("uuid") is not None
        return created_uuid


    def test_update_node(self, generic_name) -> None:
        note = "mens et manus"
        node = cript.Project(name=generic_name, notes=note)
        assert node.get("notes") == note

    def test_method_find_by_uuid(self, project_uuid, generic_name) -> None:
        node = cript.Project(uuid=project_uuid)
        assert node.get("name") == generic_name

    def test_create_project(self) -> None:
        node = cript.Project(
            name=f"proj{uuid4()}",
            notes="my notes",
        )
        assert node.get("name") is not None

    def test_create_collection_exisiting_project(self, generic_collection, project_uuid) -> None:
        col1=cript.Collection(name=generic_collection)
        proj = cript.Project(uuid=project_uuid, collection=[col1])
        # TODO I expect this to work
        # assert proj.collection[0].name == generic_collection
        assert col1.get("uuid") is not None

    def test_create_experiment_exisiting_collection(self, generic_experiment, generic_collection, project_uuid) -> None:
        exp1 = cript.Experiment(name=generic_experiment)
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        exp1.name == generic_experiment
        # TODO this will have to work too
        # assert col1.experiment[0].name == generic_experiment
        # assert proj1.collection[0].experiment[0].name == generic_experiment


    def test_create_material(self, project_uuid, generic_material1) -> None:
        comp_forcefield= cript.ComputationalForcefield(key="mmff", building_block="atom")
        material_name2 = f"mat_{uuid4()}"
        mat2 = cript.Material(name=material_name2)
        proj1 = cript.Project(uuid=project_uuid, material=[mat2])
        mat1 = cript.Material(
            name=generic_material1,
            bigsmiles="{[][<]CCO[>][]}",
            computational_forcefield=comp_forcefield,
            component=[mat2]
        )
        proj1 = cript.Project(uuid=project_uuid, material=[mat1])
        assert mat1.get("name") == generic_material1
        # TODO this needs to work
        # material_names = [mat.name for mat in proj1.material]
        # assert generic_material1 in material_names
        # assert material_name2 in material_names

    def test_create_material_property(self, project_uuid, generic_material1) -> None:
        prop1 = cript.Property(key="air_flow", type="number", unit="L/s", value=1)
        mat1 = cript.Material(name=generic_material1, property=[prop1])
        proj1 = cript.Project(uuid=project_uuid, material=[mat1])
        assert prop1.get("uuid") is not None


    def test_create_inventory(self, generic_material1, generic_inventory, generic_collection, project_uuid) -> None:
        mat1 = cript.Material(name=generic_material1)
        mat2 = cript.Material(name=f"mat_{uuid4()}")
        inv1 = cript.Inventory(name=generic_inventory, material=[mat1, mat2])
        col1 = cript.Collection(name=generic_collection, inventory=[inv1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1], material=[mat1, mat2])
        assert inv1.get("uuid") is not None


    def test_create_computation(self, generic_computation, generic_experiment, generic_collection, project_uuid) -> None:
        comp1 = cript.Computation(name=generic_computation, type="MC")
        exp1 = cript.Experiment(name=generic_experiment, computation=[comp1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert comp1.get("uuid") is not None


    def test_create_computation_software(self, generic_computation, generic_experiment, generic_collection, project_uuid) -> None:
        soft1 = cript.SoftwareConfiguration()
        comp1 = cript.Computation(name=generic_computation, type="MC", software_configuration=[soft1])
        exp1 = cript.Experiment(name=generic_experiment, computation=[comp1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert comp1.get("uuid") is not None


    def test_create_computation_process(self, generic_experiment, generic_collection, project_uuid) ->None:
        file1 = cript.File(type=f"logs", source="https://criptapp.org/file1.txt")
        input_data1 = cript.Data(type="nmr_h1", file=[file1])
        file2=cript.File(type=f"logs", source="https://criptapp.org/file2.txt")
        output_data1 = cript.Data(type="nmr_h1", file=[file2])
        comp_process1 = cript.ComputationProcess(name="compr1", type="reaction", input_data=[input_data1], output_data=[output_data1])

        exp1 = cript.Experiment(name=generic_experiment, computation_process=[comp_process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert comp_process1.get("uuid") is not None


    def test_create_process(self, generic_process, generic_experiment, generic_collection, project_uuid) -> None:
        process1 = cript.Process(name=generic_process, type="mix")
        exp1 = cript.Experiment(name=generic_experiment, process=[process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert process1.name == generic_process
        assert process1.uuid is not None

    def test_create_ingredient(self, generic_material1, generic_process, generic_experiment, generic_collection, project_uuid) -> None:
        mat1 = cript.Material(name=generic_material1)
        qnt1 = cript.Quantity(key="mass", value=2, unit="kg")
        ingredient = cript.Ingredient(material=mat1, quantity=[qnt1])
        process1 = cript.Process(name=generic_process, type="mix")
        exp1 = cript.Experiment(name=generic_experiment, process=[process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1], material=[mat1])
        assert process1.get("name") == generic_process
        assert process1.get("uuid") is not None

    def test_create_algorithm(self, generic_computation, generic_experiment, generic_collection, project_uuid) -> None:
        algorithm1 = cript.Algorithm(key="advanced_sampling", type="analysis")
        software1 = cript.Software(name="Test", version="1.0")
        soft1 = cript.SoftwareConfiguration(software=software1, algorithm=[algorithm1])
        comp1 = cript.Computation(name=generic_computation, type="MC", software_configuration=[soft1])
        exp1 = cript.Experiment(name=generic_experiment, computation=[comp1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert algorithm1.get("uuid") is not None

    def test_create_citation(self, generic_experiment, generic_collection, project_uuid) -> None:
        ref1 = cript.Reference(type="web_site", title="https://app.criptapp.org")
        cit1 = cript.Citation(type="reference", reference=ref1)
        process1 = cript.Process(name="process1", type="mix", citation=[cit1])
        exp1 = cript.Experiment(name=generic_experiment, process=[process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert cit1.get("uuid") is not None

    def test_create_reference(self, generic_experiment, generic_collection, project_uuid) -> None:
        ref1 = cript.Reference(type="web_site", title="https://app.criptapp.org")
        cit1 = cript.Citation(type="reference", reference=ref1)
        process1 = cript.Process(name="process1", type="mix", citation=[cit1])
        exp1 = cript.Experiment(name=generic_experiment, process=[process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert ref1.get("uuid") is not None

    def test_create_computational_forcefield(self, project_uuid) -> None:
        comp_forcefield= cript.ComputationalForcefield(key="mmff", building_block="atom")
        mat1 = cript.Material(
            name=f"mat_{uuid4()}",
            bigsmiles="{[][<]CCO[>][]}",
            computational_forcefield=comp_forcefield,
        )
        proj1 = cript.Project(uuid=project_uuid, material=[mat1])
        assert comp_forcefield.get("uuid") is not None

    def test_create_condition(self, generic_experiment, generic_collection, project_uuid) -> None:
        cond1 = cript.Condition(key="energy", type="type", value=1)
        process1 = cript.Process(name="process1", type="mix", condition=[cond1])
        exp1 = cript.Experiment(name=generic_experiment, process=[process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert cond1.get("uuid") is not None

    def test_create_data(self, generic_experiment, generic_collection, project_uuid) ->None:
        file1 = cript.File(type=f"logs", source="https://criptapp.org/file1.txt")
        data1 = cript.Data(type="nmr_h1", file=[file1])

        exp1 = cript.Experiment(name=generic_experiment, data=[data1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert data1.get("uuid") is not None

    def test_create_file(self, generic_experiment, generic_collection, project_uuid) ->None:
        file1 = cript.File(type=f"logs", source="https://criptapp.org/file1.txt")
        data1 = cript.Data(type="nmr_h1", file=[file1])
        # TODO add test for s3
        exp1 = cript.Experiment(name=generic_experiment, data=[data1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert file1.get("uuid") is not None

    def test_create_equipment(self, generic_experiment, generic_collection, project_uuid) -> None:
        equip1 = cript.Equipment(key="burner")
        process1 = cript.Process(name="process1", type="mix", equipment=[equip1])
        exp1 = cript.Experiment(name=generic_experiment, process=[process1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert equip1.get("uuid") is not None

    def test_create_parameter(self, generic_computation, generic_experiment, project_uuid, generic_collection) -> None:
        param1 = cript.Parameter(key="bond_type", value="1")
        algorithm1 = cript.Algorithm(key="advanced_sampling", type="analysis", parameter=[param1])
        software1 = cript.Software(name="Test", version="1.0")
        soft1 = cript.SoftwareConfiguration(software=software1, algorithm=[algorithm1])
        comp1 = cript.Computation(name=generic_computation, type="MC", software_configuration=[soft1])
        exp1 = cript.Experiment(name=generic_experiment, computation=[comp1])
        col1 = cript.Collection(name=generic_collection, experiment=[exp1])
        proj1 = cript.Project(uuid=project_uuid, collection=[col1])
        assert param1.get("uuid") is not None

    def test_delete_attribute(self, project_uuid) -> None:
        proj1 = cript.Project(uuid=project_uuid)
        proj1.delete(notes=None)
        # I don't think this test is sufficient, we should verify that it also does not exist on the backend
        assert not hasattr(proj1, 'notes')

    def test_unlink_child(self, project_uuid) -> None:
        mat1 = cript.Material(name=f"mat_{uuid4()}")
        proj1 = cript.Project(uuid=project_uuid, material=[mat1])
        proj1.delete(material=[mat1])
        assert not any(mat1.get("uuid") == l.get("uuid") for l in proj1.material)

    def test_unlink_all_children(self, project_uuid) -> None:
        mat1 = cript.Material(name=f"mat_{uuid4()}")
        proj1 = cript.Project(uuid=project_uuid, material=[mat1])
        proj1.delete(material=None)
        assert proj1.get("material") is None

    def test_delete_node(self, project_uuid) -> None:
        # Maybe we should be a little careful with this test.
        # It depends on the order of execution of tests.
        # This could get flaky
        proj1 = cript.Project(uuid=project_uuid)
        proj1.delete()
        assert proj1.get("uuid") is None

    def test_delete_unitialized_node(self, generic_collection) -> None:
        col1 = cript.Collection(name=generic_collection)
        with pytest.raises(ValueError):
            col1.delete()
