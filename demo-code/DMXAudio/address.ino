
const uint8_t numAddressPins = 9;
const uint8_t addressPins[9] = {33, 34, 35, 36, 37, 38, 39, 40, 41};

void address_setup(void)
{
  for (uint8_t i = 0; i < numAddressPins; i++)
  {
    pinMode(addressPins[i], INPUT_PULLUP);
  }
}

uint16_t address_get(void)
{
  uint16_t tmp = 0;

  for (uint8_t i = 0; i < numAddressPins; i++)
  {
    if (!digitalRead(addressPins[i]))
    {
      tmp += (1 << i);
    }
  }

  return tmp;
}
