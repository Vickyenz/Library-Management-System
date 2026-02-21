import gradio as gr
from library.service import LibraryService

service = LibraryService()

def ui_add(title, b_id, author):
    return service.add_item(title, b_id, author), service.display_all()

def ui_remove(b_id):
    return service.remove_item(b_id), service.display_all()

def ui_toggle(b_id):
    return service.toggle_status(b_id), service.display_all()


with gr.Blocks(title="Library System") as demo:
    gr.Markdown("# 📚 Library Management Web App")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### ➕ Add Book")
            t_input = gr.Textbox(label="Title")
            a_input = gr.Textbox(label="Author")
            id_input = gr.Textbox(label="Book ID")
            add_btn = gr.Button("Add Book", variant="primary")

        with gr.Column():
            gr.Markdown("### ⚙ Manage Book")
            manage_id = gr.Textbox(label="Book ID")
            with gr.Row():
                status_btn = gr.Button("Check In/Out")
                remove_btn = gr.Button("Delete Book", variant="stop")

    gr.Markdown("### 📖 Catalog")
    output_display = gr.Textbox(lines=12, interactive=False)
    message_box = gr.Textbox(label="System Message", interactive=False)

    add_btn.click(ui_add, [t_input, id_input, a_input], [message_box, output_display])
    remove_btn.click(ui_remove, [manage_id], [message_box, output_display])
    status_btn.click(ui_toggle, [manage_id], [message_box, output_display])


demo.launch(server_name="0.0.0.0", server_port=7860)
