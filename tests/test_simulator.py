import pytest
from src.simulator.simulate_iot import generate_event

def test_generate_event():
    event = generate_event()
    
    assert "device_id" in event
    assert "temp" in event
    assert "humidity" in event
    assert "timestamp" in event
    
    assert isinstance(event["temp"], float)
    assert 20 <= event["temp"] <= 35
    assert 40 <= event["humidity"] <= 80
    assert len(event["device_id"]) > 0