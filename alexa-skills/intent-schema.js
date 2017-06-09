{
  "intents": [
    {
      "slots": [
        {
          "name": "status",
          "type": "GPIO_CONTROL"
        },
        {
          "name": "pin",
          "type": "AMAZON.NUMBER"
        }
      ],
      "intent": "GPIOControlIntent"
    },
    {
      "slots": [
        {
          "name": "status",
          "type": "GPIO_CONTROL"
        },
        {
          "name": "device",
          "type": "TANK_CONTROL"
        }
      ],
      "intent": "FishTankDeviceIntent"
    },
    {
      "slots": [
        {
          "name": "phrase",
          "type": "PHRASE_CONTROL"
        }
      ],
      "intent": "FishTankPhraseIntent"
    }
  ]
}
