from dataclasses import dataclass

import pytest

pydantic = pytest.importorskip("pydantic")

from eventbus.data.actor_ref import ActorRef
from game.service.scene.scene_instructions import SceneInstructions


@dataclass
class DummyNpc:
    actor_ref: ActorRef


def test_scene_instructions_parses_poi_and_instruction(tmp_path):
    path = tmp_path / "instructions.txt"
    path.write_text(
        "poi travel,Go to door,1,2,3,door_ref\n"
        "npc_1 Hello there\n",
        encoding="utf-8",
    )

    config = SceneInstructions.Config(file=str(path), encoding="utf-8")
    scene = SceneInstructions(config, enable_keyboard_listener=False)

    npc = DummyNpc(
        actor_ref=ActorRef(ref_id="npc_1", type="npc", name="Test NPC", female=False)
    )

    instruction = scene.get_next_manual_instruction_for_pick_npc([npc])

    assert instruction is not None
    assert instruction.actor_to_act.ref_id == "npc_1"
    assert instruction.reason == "Hello there"
    assert instruction.pass_reason is True

    assert len(scene.pois) == 1
    assert scene.pois[0].label == "Go to door"
    assert scene.pois[0].pos == [1.0, 2.0, 3.0]
    assert scene.pois[0].ref_id == "door_ref"

    assert path.read_text(encoding="utf-8").startswith("# npc_1 Hello there")


def test_scene_instructions_hold_pauses_processing(tmp_path):
    path = tmp_path / "instructions.txt"
    path.write_text("hold\nnpc_1 Next line\n", encoding="utf-8")

    config = SceneInstructions.Config(file=str(path), encoding="utf-8")
    scene = SceneInstructions(config, enable_keyboard_listener=False)

    npc = DummyNpc(
        actor_ref=ActorRef(ref_id="npc_1", type="npc", name="Test NPC", female=False)
    )

    assert scene.get_next_manual_instruction_for_pick_npc([npc]) is None
    assert scene._manually_instructed_to_hold_on_instructions is True

    contents = path.read_text(encoding="utf-8")
    assert contents.startswith("# hold")
