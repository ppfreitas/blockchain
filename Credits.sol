pragma solidity ^0.5;

contract Credits {

	//Define contract structure to store sensor's data
	struct SensorReading {
	uint time;
	uint sensor_id;
	uint energy;
	//bool polluting;
	}

	//map reading id with data
	mapping(uint => SensorReading) public readings;

	//transaction id
	uint public trans_id;

	//uint public amount;

	// func to add reading to struc
	function addReading(uint _time, uint _sensor, uint _mwh) public {
		trans_id++; //increment id count
		readings[trans_id] = SensorReading(_time, _sensor, _mwh);
/*
		if (_polluting = true) {
			amount = _mwh*1;
			require(msg.sender.balance > amount);
			msg.sender.transfer(amount);
		}

		if (_polluting = false) {
			amount = _mwh*2;
			require(address(this).balance > amount);
			address(this).transfer(msg.value);
		}*/
	}

	function getReadInfo(uint _trans_id) public view returns (uint, uint, uint) {
		return (readings[_trans_id].time, readings[_trans_id].sensor_id, readings[_trans_id].energy);
	}

	// initialize contract
	constructor() public {
	trans_id = 1;
	SensorReading(0, 0, 0);
	}

}
