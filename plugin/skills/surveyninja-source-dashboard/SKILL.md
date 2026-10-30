---
name: surveyninja-source-dashboard
description: "Compares where SurveyNinja survey respondents came from and which
  channels perform best, using the unique links or source labels given to each
  channel. Use when someone asks which email, post, ad or campaign worked, wants
  responses broken down by source or channel, or compares channels by completion
  and response quality."
---

# Where they came from and what it gave

A survey is usually shared in several places at once. Responses can be split by
channel only if each channel got its own set of unique links or its own link
with a source label.

Reply to the person in the language they write in.

## Check there is something to compare

- `manage_quiz_unique_links` with `list_groups`: whether the channels got their
  own sets of unique links.
- `get_quiz_variables`: the link variables set up in the survey. A source label
  is usually one of them, such as `source` or `utm_source`. A label is saved with
  the response even when no variable was set up for it, so also look at
  `extra_fields` in a few responses from `get_quiz_answers`, or ask which
  parameter the links carried.
- `get_answer_extra_field_values` with that name as `key` lists the values that
  arrived. It is not on every plan; the `extra_fields` of responses show the same
  on any plan.

If there are neither unique links nor labels, there is nothing to compare: **they
cannot be added retroactively**. Say so plainly and suggest giving each channel
its own link next time.

Visits that Google Analytics or Meta Pixel count for the survey stay in those
services and are not visible through these tools. This breakdown comes only from
unique links and labels on responses; for traffic numbers, the person reads their
analytics.

## Collect

Per channel you need: how many arrived, how many finished, and the target metric
(contacts, average rating, whatever matters here).

Count them from `get_quiz_answers`, paged with `offset` (up to 100 per page):
each response carries its `extra_fields` (the labels) and its `unique_link`, and
`unique_link_group_id` narrows the list to one set of unique links. Read
`is_complete` true, then false, and group the responses by label or link
yourself. `answer_total_count` is the total for the whole survey, not for the
filtered list: count the responses you received.

Unfinished responses are kept only if the plan keeps them. Without that,
`is_complete` false quietly returns completed ones: check `is_complete` on each
response, and if there are no unfinished ones, say that completion per channel
cannot be measured.

The target metric comes from the answers inside those responses. For unique links
there is also `generate_filtered_report` with `unique_link_group_id` (and
`unique_link_ids` for single links): the same report per channel, completed
responses only. No tool builds the report for one label value; in the app that is
the Hidden Variables filter in Results.

## How to present

A table by channel, sorted by what matters to the person: channel, responses,
completion share, target metric.

Below it, three conclusions:

- **Where the most responses came from.** Obvious, and the least useful.
- **Where completion is best.** A channel can bring few people but good ones.
- **Where responses are worse.** Sometimes the cause is the promise in the ad
  rather than the channel: the wrong people arrived.

## Worth stating

- **Volume and quality are different things.** A thousand people at five percent
  completion is worse than a hundred at fifty.
- **Do not compare small channels head-on with large ones**: at twenty responses
  the share jumps around.
- **Responses with no label** deserve their own row instead of "other": usually
  direct visits or a label lost when the link was forwarded.

## What not to do

- **Do not infer the channel from arrival time.** No label means no answer.
- **Do not advise switching a channel off** after a single run.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
