from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    freeform1 = request.form.get('input_freeform1', '')
    freeform2 = request.form.get('input_freeform2', '')
    freeform3 = request.form.get('input_freeform3', '')
    freeform4 = request.form.get('input_freeform4', '')
    freeform6 = request.form.get('input_freeform6', '')
    freeform7 = request.form.get('input_freeform7', '')
    freeform8 = request.form.get('input_freeform8', '')
    freeform9 = request.form.get('input_freeform9', '')
    freeform10 = request.form.get('input_freeform10', '')
    freeform11 = request.form.get('input_freeform11', '')
    freeform12 = request.form.get('input_freeform12', '')
    return render_template("main_page.html", output= f"Arrr! Ahoy there {name}. Ye can always pretend to be a bloodthirsty {freeform}, threatening everyone by waving yer {freeform1} sword in the air, but until ye learn to {freeform2} like a pirate, ye'll never be {freeform3} accepted as an authentic {freeform4}. So here's what ye do: Cleverly work into yer daily conversations some pirate phrases such as \"Ahoy there, {freeform6},\" \"Avast, ye {freeform7},\" and \"Shiver me {freeform8}.\" Remember to drop all yer \"g\"'s when ye say such words as sailin', spittin', and fightin'. This will give ye a/an {dropdown} start to being recognized as a swashbucklin' {freeform9}. Once ye have the lingo down pat, it helps to wear a three-cornered {freeform10} on yer head, stash a/an {freeform11} in yer pants, and keep a/an {freeform12} perched atop yer {select}. Aye, now ye be a real pirate!")
