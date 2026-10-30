<sub><a href="../README.md">SurveyNinja MCP</a> › Tools</sub>

# SurveyNinja MCP tools

173 tools by section. 62 only read. 29 delete or overwrite data and carry the
`destructiveHint` annotation, so your client can ask before it calls them. The rest create or change data, and
some act at once: publishing a survey or inviting a member, for example.

7 tools work only when you connect with an API key and are marked *API key only*. An **Allow access**
connection, the one Claude, ChatGPT and other assistant apps use, does not list them: account settings, and
anything that sends responses to a new outside address (creating or changing a webhook, confirming a new email
recipient). Those are set up in the app.

Your client gets the server's own list with `tools/list` when it connects. Tool names say `quiz` where the app
says survey: they mean the same thing.

[Surveys](#surveys) <sub>18</sub> &nbsp;|&nbsp; [Questions and logic](#questions-and-logic) <sub>10</sub> &nbsp;|&nbsp; [Variables and hidden fields](#variables-and-hidden-fields) <sub>12</sub> &nbsp;|&nbsp; [Themes](#themes) <sub>6</sub> &nbsp;|&nbsp; [Sharing](#sharing) <sub>7</sub> &nbsp;|&nbsp; [Promo codes](#promo-codes) <sub>6</sub> &nbsp;|&nbsp; [Online booking](#online-booking) <sub>8</sub> &nbsp;|&nbsp; [Answers](#answers) <sub>11</sub> &nbsp;|&nbsp; [Reports](#reports) <sub>21</sub> &nbsp;|&nbsp; [Exports](#exports) <sub>7</sub> &nbsp;|&nbsp; [Notifications and email](#notifications-and-email) <sub>14</sub> &nbsp;|&nbsp; [Integrations and webhooks](#integrations-and-webhooks) <sub>15</sub> &nbsp;|&nbsp; [Folders](#folders) <sub>4</sub> &nbsp;|&nbsp; [Team and roles](#team-and-roles) <sub>12</sub> &nbsp;|&nbsp; [Account and workspace](#account-and-workspace) <sub>16</sub> &nbsp;|&nbsp; [Plan and partners](#plan-and-partners) <sub>5</sub> &nbsp;|&nbsp; [Email campaigns](#email-campaigns) <sub>1</sub>

## Surveys

| Tool | What it does | Kind |
|---|---|---|
| `create_quiz` | Create quiz | write |
| `create_quiz_from_template` | Create quiz from template | write |
| `generate_ai_quiz` | Build quiz from description | write |
| `search_quiz_templates` | Search ready-made quizzes | read |
| `get_workspace_templates` | Workspace templates | read |
| `make_quiz_template` | Make quiz a template | write |
| `get_quiz_list` | Quiz list | read |
| `duplicate_quiz` | Duplicate quiz | write |
| `rename_quiz` | Rename quiz | write |
| `move_quiz` | Move quiz to a folder | write |
| `archive_quiz` | Archive quiz | write |
| `delete_quiz` | Delete quiz | destructive |
| `restore_quiz` | Restore quiz from trash | write |
| `publish_quiz` | Publish quiz | write |
| `get_quiz_versions` | Quiz publication history | read |
| `restore_quiz_version` | Restore previous quiz version | write |
| `update_quiz_note` | Quiz note | write |
| `update_quiz_settings` | Quiz settings | write |

## Questions and logic

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_structure` | Quiz structure | read |
| `update_quiz_widgets` | Quiz questions and structure | write |
| `update_quiz_logic` | Quiz branching logic | write |
| `get_quiz_texts` | Quiz default texts | read |
| `update_quiz_texts` | Edit default texts | write |
| `upload_quiz_media` | Upload a file to a quiz | write |
| `upload_quiz_widget_image` | Image for an answer option | write |
| `get_favorite_questions` | Favorite questions | read |
| `save_favorite_question` | Save question to favorites | write |
| `delete_favorite_question` | Delete favorite question | destructive |

## Variables and hidden fields

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_variables` | Quiz variables | read |
| `create_quiz_variable` | Create quiz variable | write |
| `update_quiz_variable` | Update quiz variable | write |
| `delete_quiz_variable` | Delete quiz variable | destructive |
| `get_quiz_hidden_options` | Quiz hidden options | read |
| `create_hidden_option` | Create quiz hidden option | write |
| `update_hidden_option` | Update quiz hidden option | write |
| `delete_hidden_option` | Delete quiz hidden option | destructive |
| `get_quiz_widgets_hidden` | Widget hidden options | read |
| `create_widget_hidden_option` | Create widget hidden option | write |
| `update_widget_hidden_option` | Update widget hidden option | write |
| `delete_widget_hidden_option` | Delete widget hidden option | destructive |

## Themes

| Tool | What it does | Kind |
|---|---|---|
| `get_theme_list` | Theme list | read |
| `get_theme_details` | Theme details | read |
| `create_theme` | Create theme | write |
| `update_theme` | Update theme | write |
| `manage_theme` | Manage themes | destructive |
| `apply_quiz_theme` | Apply theme to quiz | write |

## Sharing

| Tool | What it does | Kind |
|---|---|---|
| `set_quiz_link` | Quiz link address | write |
| `manage_quiz_qr_code` | Quiz QR code | write |
| `manage_quiz_passwords` | Passwords for a closed quiz | destructive |
| `export_quiz_print` | Quiz print version | read |
| `manage_quiz_unique_links` | Unique quiz links | destructive |
| `get_share_links` | List public links | read |
| `set_share_link_active` | Disable or enable a public link | destructive |

## Promo codes

| Tool | What it does | Kind |
|---|---|---|
| `create_promocode_group` | Create promocode list | write |
| `manage_promocode_group` | Manage promocode list | destructive |
| `add_promocodes` | Add promocodes | write |
| `get_promocode_list` | Promocode lists | read |
| `get_promocode_codes` | Promocode list codes | read |
| `get_promocode_list_quizzes` | Quizzes of a promocode list | read |

## Online booking

| Tool | What it does | Kind |
|---|---|---|
| `create_booking_block` | Block booking time | write |
| `delete_booking_block` | Remove booking block | destructive |
| `get_booking_journal` | Booking journal | read |
| `update_booking` | Update a booking | write |
| `get_schedulers` | Booking schedules | read |
| `save_scheduler` | Booking schedule | write |
| `duplicate_scheduler` | Duplicate booking schedule | write |
| `delete_scheduler` | Delete booking schedule | destructive |

## Answers

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_answers` | Quiz answers | read |
| `count_quiz_answers` | How many answers match | write |
| `get_answer_extra_field_values` | Link label values | read |
| `tag_answer` | Tags on an answer | write |
| `get_answer_tags` | Account answer tags | read |
| `create_answer_tag` | Create answer tag | write |
| `delete_answer_tag` | Delete answer tag | destructive |
| `set_answer_note` | Answer note | write |
| `toggle_answer_visibility` | Hide an answer from reports | write |
| `set_answers_order_mode` | Question order in an answer | write |
| `delete_quiz_answers` | Delete answers | destructive |

## Reports

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_report` | Quiz report | read |
| `generate_filtered_report` | Filtered report | write |
| `get_quiz_report_filters` | Saved report filters | read |
| `save_quiz_report_filters` | Save report filters | write |
| `get_quiz_report_files` | Files from answers | read |
| `get_quiz_report_inputs` | Text answers of a question | read |
| `generate_ai_report` | AI report | write |
| `get_ai_report` | Ready AI report | read |
| `share_ai_report` | Public link to an AI report | write |
| `share_report_link` | Public link to a report | write |
| `share_summary_link` | Public link to a summary | write |
| `share_answers_link` | Public link to answers | write |
| `get_workspace_report_appearance` | Workspace report appearance | read |
| `create_report_appearance_preset` | Create report appearance preset | write |
| `delete_report_appearance_preset` | Delete report appearance preset | destructive |
| `update_workspace_report_palette` | Workspace report palette | write |
| `get_quiz_visits` | Visit log | read |
| `get_quiz_visit_segments` | Visits by source, device, browser or country | read |
| `reset_quiz_visits` | Reset visits | destructive |
| `manage_quiz_filter_presets` | Saved filters | write |

## Exports

| Tool | What it does | Kind |
|---|---|---|
| `export_answers_csv` | Export answers to CSV | read |
| `export_answers_xlsx` | Export answers to Excel | read |
| `export_answers_spss` | Export answers to SPSS | read |
| `export_answers_word` | Export answers to Word | read |
| `export_summary_pdf` | Export summary to PDF | read |
| `export_filtered_report_pdf` | Export report to PDF | read |
| `export_filtered_report_word` | Export report to Word | read |

## Notifications and email

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_email_settings` | Quiz email settings | read |
| `toggle_quiz_email` | Quiz emails on and off | write |
| `add_quiz_email_recipient` | Add answer copy recipient | write |
| `confirm_quiz_email_recipient` | Confirm recipient address | write, *API key only* |
| `toggle_quiz_email_recipient` | Recipient on and off | write |
| `delete_quiz_email_recipient` | Delete answer copy recipient | destructive |
| `save_quiz_email_template` | Quiz email template | write |
| `set_quiz_email_questions` | Questions included in the email | write |
| `manage_workspace_smtp` | Custom mail service | write |
| `add_quiz_email_team_member` | Account member as a recipient | write |
| `save_quiz_email_notifications` | Email rules, digest and events | write |
| `send_quiz_email_test` | Send me a sample letter | write |
| `get_quiz_email_log` | Quiz email log | read |
| `resend_quiz_email_log` | Send the letter again | write |

## Integrations and webhooks

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_integrations` | Quiz integration state | read |
| `get_integration_logs` | Messenger delivery log | read |
| `resend_integration_logs` | Resend to messenger | write |
| `manage_quiz_google_sheets` | Google Sheets export | destructive |
| `manage_quiz_messenger` | Telegram notifications | destructive |
| `get_quiz_messenger_link` | Bot connection link | read |
| `manage_quiz_zapier` | Sending to Zapier | write |
| `manage_quiz_analytics` | Analytics counters and pixels | write |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `create_quiz_webhook` | Create webhook | write, *API key only* |
| `update_quiz_webhook` | Update webhook | write, *API key only* |
| `toggle_quiz_webhook` | Webhook on and off | write |
| `delete_quiz_webhook` | Delete webhook | destructive |
| `get_quiz_webhook_logs` | Webhook delivery log | read |
| `resend_quiz_webhook_log` | Resend webhook | write |

## Folders

| Tool | What it does | Kind |
|---|---|---|
| `get_folder_list` | Folder list | read |
| `create_folder` | Create folder | write |
| `manage_workspace_folder` | Manage folder | destructive |
| `manage_folder_access` | Folder access | destructive |

## Team and roles

| Tool | What it does | Kind |
|---|---|---|
| `get_workspace_members` | Workspace members | read |
| `invite_workspace_member` | Invite member | write |
| `resend_workspace_member_invite` | Resend member invite | write |
| `remove_workspace_member` | Remove member | destructive |
| `set_workspace_member_role` | Change member role | write |
| `set_workspace_member_folders` | Folders available to a member | write |
| `get_workspace_member_access` | Member access | read |
| `get_workspace_roles` | Member roles | read |
| `save_workspace_role` | Member role | write |
| `delete_workspace_role` | Delete member role | destructive |
| `set_workspace_member_blocked` | Close or restore member access | destructive |
| `set_workspace_member_api_access` | Member API access | destructive |

## Account and workspace

| Tool | What it does | Kind |
|---|---|---|
| `get_user_me` | My profile | read |
| `update_user_profile` | Update my profile | write, *API key only* |
| `manage_user_sessions` | Account sessions | destructive, *API key only* |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_details` | Workspace details | read |
| `get_workspace_activity` | Account activity log | read |
| `update_workspace_branding` | Workspace logo and copyright | write |
| `upload_workspace_logo` | Upload workspace logo | write |
| `delete_workspace_logo` | Delete workspace logo | destructive |
| `manage_workspace_domain` | Custom account domain | write |
| `get_workspace_domain_status` | Custom domain status | read |
| `manage_workspace_files` | Workspace files | destructive |
| `get_workspace_hidden_files` | Files hidden over quota | read |
| `get_workspace_storage` | Custom file storage | read |
| `get_workspace_storage_usage` | Storage usage | read |
| `verify_workspace_storage` | Verify custom storage | write |

## Plan and partners

| Tool | What it does | Kind |
|---|---|---|
| `get_workspace_tariff` | Workspace plan | read |
| `get_tariff_list` | Plan list | read |
| `get_partner_program` | Partner program | read, *API key only* |
| `manage_partner_source` | Partner source labels | write, *API key only* |
| `get_respondent_campaigns` | Ordered respondents | read |

## Email campaigns

| Tool | What it does | Kind |
|---|---|---|
| `get_mailing_state` | Mailing state | read |
