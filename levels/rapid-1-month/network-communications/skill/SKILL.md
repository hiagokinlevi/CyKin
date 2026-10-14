---
name: oca-network-communications-rapid-74df54f0
description: "Guide a learner through the published rapid network book: twenty English chapters, two synthetic labs, and EX001–EX066. Review is still open."
license: CC0-1.0
---

# Network and communications security — Rapid course course skill

Use this **one skill for the whole 1 month course**. The English manuscript publishes twenty chapter-lessons. Other language folders are working outlines, not translations of those twenty English chapters. Read the actual manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 011, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/network-communications/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): twenty chapters, two labs and EX001–EX066. Review remains open. This is not a finished qualification.

## Navigation rule

At the end of an authored chapter, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. The course chapter index connects its final row to the next course in the same language.

## Twenty-chapter rapid route

This is the one-month **rapid course** in network and communications security. The book follows synthetic learner **Leo Hart**, coached by **Nadia Petrov** at the fictional **Quayside Skills Centre**, as he helps **Ellen** at the fictional **Bramble Street Bakery**, one shop. Lessons 1–4 teach the shared network, the written scope, the lease comparison, and the router checklist. Lessons 5–20 teach the mechanisms those prints do not settle. The supplementary WAF project is not this bakery and is not a control the checklist measured.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Foundations, scope, permission and safe practice | EX001–EX026 |
| 3–4 | Leases, dependencies, the checklist and the report | lab_leases.py; lab_router.py; EX027–EX050 |
| 5–20 | One mechanism or evidence limit each | EX051–EX066 |

Verified lab facts (synthetic). Do not say either print was replaced.

```text
aa:01  192.168.1.10  till-1
aa:02  192.168.1.11  till-2
aa:03  192.168.1.20  office-pc
aa:05  192.168.1.30  owner-phone
bb:77  192.168.1.41  UNKNOWN
aa:04  192.168.1.12  card-reader
cc:19  192.168.1.42  UNKNOWN
unknown: ['bb:77', 'cc:19']  known but not seen: []
```

```text
FIX   admin password changed from default
PASS  Wi-Fi uses WPA2 or WPA3
PASS  guest network enabled
FIX   guest isolated from business devices
FIX   remote administration off
FIX   firmware updated within 180 days
FIX   UPnP off
2 of 7 pass
```

## Teaching guardrails

- Do not edit `lab_leases.py` or `lab_router.py`. Do not print a second lease table or a script that says 7 of 7.
- The lease run is synthetic practice. A live export is mentioned and not pasted. `bb:77` and `cc:19` stay UNKNOWN on the print. The speaker and the scanner are Ellen's later names. No staff name, company name, or third device is added. `known but not seen` stays empty.
- The hardware tokens are abbreviated. Do not expand them or treat a lookup as authentication. DHCP assigns an address; it does not prove who holds the device.
- All seven addresses begin `192.168.1` and sit in RFC 1918's `192.168.0.0/16`. No mask and no public address are printed. Private addressing is not inside isolation.
- The Wi-Fi string stays `WPA2-Personal`. The mode check also accepts WPA3-Personal, which is not the stored value. Personal mode is one shared passphrase. No passphrase is written. No per-person wireless account is recorded.
- Guest existence passes and `guest_isolated_from_lan` stays false in the script. The later move of the speaker and scanner stays prose.
- Remote administration stays true in the script. No host, port, or URL is added. Do not describe how to reach a management page.
- Firmware age stays 540 against a threshold of 180. About eighteen months is the gloss. No version, date, or vulnerability identifier is added.
- UPnP stays true in the script. No port, payload, or requester is named. Do not import an outside study's percentage.
- The before score is one reading: 2 of 7. The two passes are the Wi-Fi mode and guest existence. The narrative seven of seven is a later reading, not this input. The five dictionary values that fail stay false, false, true, 540, and true.
- Card data stays on the path from the reader to the provider and off the office computer. TLS and HTTPS are channel protection, not a LAN boundary. No resolver or DNSSEC deployment is printed.
- The isolation check is Leo's phone, the internet, and the office computer, with permission. No command, capture, scan, other target, or detection rate is added. No log line and no flow export are invented.
- Five habits stay five. No calendar date is printed. No second run is attached. The provider owns the router and the payment company owns the reader.
- BCP 38, route authorisation, IPsec, and zero trust are not rows in this checklist. Do not score them. One shop stays one shop.
- Do not teach exploit steps, payloads, scanning, or bypasses. Defender-side synthetic material only.
- After chapter 20 the next stop in this level is course 012. Do not call the bakery secure. Twenty lessons meet the planning minimum and leave review open.

## Continue the curriculum

After chapter 20, the next stop is [course 012: Systems, endpoints and hardware security / Rapid course](../../systems-endpoints-hardware/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and EX001–EX066 are published, and independent review remains open. Page count is not the writing target. This is not a finished qualification. Other language folders keep their own state until their own writing and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
