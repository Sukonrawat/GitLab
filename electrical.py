import argparse
import math


def analyze_dc(voltage_v: float, resistance_ohm: float) -> dict[str, float]:
    """คำนวณกระแสและกำลังไฟฟ้าสำหรับวงจร DC อย่างง่าย."""
    try:
        voltage = float(voltage_v)
        resistance = float(resistance_ohm)
    except (TypeError, ValueError) as error:
        raise ValueError("แรงดันและความต้านทานต้องเป็นตัวเลข") from error

    if not math.isfinite(voltage):
        raise ValueError("แรงดันต้องเป็นค่าจำกัด")
    if not math.isfinite(resistance) or resistance <= 0:
        raise ValueError("ความต้านทานต้องเป็นค่าจำกัดที่มากกว่า 0 โอห์ม")

    # ...existing code... สมการคำนวณเดิมตามกฎของโอห์ม
    current_a = voltage / resistance
    power_w = voltage * current_a

    if not math.isfinite(current_a) or not math.isfinite(power_w):
        raise ValueError("ผลลัพธ์เกินช่วงที่โปรแกรมคำนวณได้")

    return {"current_a": current_a, "power_w": power_w}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="คำนวณกระแสและกำลังไฟฟ้าของวงจร DC"
    )
    parser.add_argument("--voltage", type=float, default=12, help="แรงดัน (V), ค่าเริ่มต้น 12")
    parser.add_argument("--resistance", type=float, default=6, help="ความต้านทาน (Ω), ค่าเริ่มต้น 6")
    args = parser.parse_args()

    try:
        result = analyze_dc(args.voltage, args.resistance)
    except ValueError as error:
        parser.error(str(error))

    print(f"แรงดัน:       {args.voltage:g} V")
    print(f"ความต้านทาน: {args.resistance:g} Ω")
    print(f"กระแส:        {result['current_a']:.4f} A")
    print(f"กำลังไฟฟ้า:   {result['power_w']:.4f} W")


if __name__ == "__main__":
    main()
    