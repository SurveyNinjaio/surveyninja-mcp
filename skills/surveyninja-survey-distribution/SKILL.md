---
name: surveyninja-survey-distribution
description: "Prepares a SurveyNinja survey for distribution: the link address, a
  QR code, labeled links per channel, passwords or unique links for restricted
  access, and a printable version. Use when someone asks how to send out a survey,
  where to get the link or QR code, how to limit who can answer, or how to tell
  which channel the responses came from."
---

# Distributing the survey

The survey is ready; the question now is how people receive it and how you later
tell where they came from.

Reply to the person in the language they write in.

## The link

Check the survey is published first (`get_quiz_versions` shows the publication
history). An unpublished survey does not open by its link.

`set_quiz_link` sets the address the survey opens at. A short, meaningful address
is easier to remember and looks safer in a message. A custom address is not on
every plan.

**Channel labels matter most here.** If the survey goes to several places, such as
an email list, social posts, a WhatsApp group and a website banner, add a label to
the link for each one: `?source=newsletter`, `?source=whatsapp`. SurveyNinja saves
the label with each answer as a hidden variable, so the responses can be split
later. Without labels everything merges and there is no way to tell what worked.
Each response from `get_quiz_answers` carries its labels in `extra_fields`.

A label is saved with the response even if no variable was set up for it. Only
logic needs the variable itself (`get_quiz_variables`, `create_quiz_variable`),
and hidden variables in logic are not on every plan.

Suggest labels up front, not after the send-out: they cannot be added to responses
that already came in.

## QR code

`manage_quiz_qr_code` for print: a table sticker, a conference slide, a flyer.
Format (PNG, SVG or EPS), size, color and background can be set. A logo in the
centre is uploaded in the app; an already uploaded one is included.

The code always leads to the survey's plain published address: it takes no
label, so responses from print arrive without one. Verify the code opens the
right page **before** printing a run.

## Restricted survey

`manage_quiz_passwords` adds passwords when the survey is not for everyone, up to
fifty per call; for more, make several passes. Different groups can get different
passwords. The password check itself is switched on with `update_quiz_settings`.

Passwords are stored in a form that cannot be read back, so hand the list to the
person when you create it.

`manage_quiz_unique_links` makes a separate address per department, branch,
partner or person, each with its own answer limit; answers remember which link was
used. Not on every plan.

## Printable version

`export_quiz_print` gives the survey as PDF, Word, HTML or plain text, optionally
with a QR code to the online version. Useful when the survey is filled in on paper
or the wording is approved with a client before launch. The download link works
for one hour.

## Order when asked "how do I send this out"

1. Check the survey is published.
2. Agree on labels for the channels named.
3. Hand over one labeled link per channel.
4. Add a QR code if there is a print channel.
5. Mention that responses can be split by channel later, by their labels.

## What not to do

- **Do not publish the survey unasked**, even if it is clearly ready.
- **Do not change the address of a survey already sent out** without warning.
  SurveyNinja redirects the old address to the new one, but only until another
  survey takes the old address, and printed QR codes depend on that redirect.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit or a
  feature is not on the plan, state the fact and stop.
