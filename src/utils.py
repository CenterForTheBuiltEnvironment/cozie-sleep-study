import json
import base64
import qrcode
from IPython.display import Image


# Onboarding payload with Cozie settings
wss_title = "Sleep (CBE, v1)"
watch_survey_url = "https://raw.githubusercontent.com/CenterForTheBuiltEnvironment/cozie-sleep-study/refs/heads/main/mattress_pad_study.json"


def generate_onboarding_payload(id_participant, id_experiment, id_password):
    payload = (
        f"{{"
        f'"id_participant": "{id_participant}",'
        f'"id_experiment": "{id_experiment}",'
        f'"wss_title": "{wss_title}",'
        f'"wss_goal": 150,'
        f'"wss_time_out": 3500,'
        f'"wss_reminder_enabeled": true,'
        f'"wss_participation_time_start": "09:00",'
        f'"wss_participation_time_end": "18:00",'
        f'"wss_participation_days": "Mo,Tu,We,Th",'
        f'"wss_reminder_interval": 60,'
        f'"pss_reminder_enabled": true,'
        f'"pss_reminder_days": "Fr",'
        f'"pss_reminder_time": "14:00",'
        f'"api_read_url": "https://d3lupjxfs7.execute-api.ap-southeast-1.amazonaws.com/prod/read-influx",'
        f'"api_read_key": " XsM7ks4lLU3JexCO8RjHG6nKq8yj9oBJ7bdI3R3R",'
        f'"api_write_url": "https://d3lupjxfs7.execute-api.ap-southeast-1.amazonaws.com/prod/write-queue",'
        f'"api_write_key": " XsM7ks4lLU3JexCO8RjHG6nKq8yj9oBJ7bdI3R3R",'
        f'"app_one_signal_app_id": "be00093b-ed75-4c2e-81af-d6b382587283",'
        f'"id_password": "{id_password}",'
        f'"api_watch_survey_url": "{watch_survey_url}",'
        f'"api_phone_survey_url": "https://docs.google.com/forms/d/e/1FAIpQLSfOj7_vVRUNDHELmwQqvpFYF5m1p6IXpXaWsQgHOF8HxuTmrw/viewform?usp=pp_url&entry.32388053={id_participant}&entry.1973683772={id_experiment}"'
        f"}}"
    )

    # Convert payload to deep link
    payload_bytes = payload.encode("ascii")
    base64_bytes = base64.b64encode(payload_bytes)
    base64_payload = base64_bytes.decode("ascii")
    deep_link_url = "cozie://param?data=" + base64_payload

    # Print deep link
    print(deep_link_url)
    print(
        "Number of characters:",
        len(deep_link_url),
        "of 2048 characters (",
        int(len(deep_link_url) / 2048 * 100),
        "%)",
    )

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(deep_link_url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(f"generated_qrcodes/qrcode_{id_participant}.png")

    return Image(
        f"generated_qrcodes/qrcode_{id_participant}.png", width=700, height=700
    )
