import { useState } from "react";
import { Camera, PackageSearch, ScanLine, ShieldCheck, UploadCloud } from "lucide-react";
import { uploadProductImage } from "./services/api";

export default function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(false);

  async function handleScan(event) {
    event.preventDefault();
    if (!file) {
      setMessage("Choose a product-label image first.");
      return;
    }
    setBusy(true);
    setMessage("");
    try {
      const result = await uploadProductImage(file);
      setMessage(result.message);
    } catch (error) {
      setMessage(error.response?.data?.detail || "Could not reach the API. Check that the backend is running.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="shell">
      <nav className="nav">
        <a className="brand" href="/">
          <span className="brand-mark"><ScanLine size={20} /></span>
          <span>ExpiryLens</span>
        </a>
        <span className="nav-note">PRODUCT LIFECYCLE INTELLIGENCE</span>
      </nav>

      <section className="hero">
        <p className="eyebrow">A smarter way to manage what you own</p>
        <h1>Know what you have.<br /><em>Before time runs out.</em></h1>
        <p className="intro">
          Turn product-label photographs into organised inventory.
          Recognise date information, review it, and keep track of your products.
        </p>
      </section>

      <section className="workspace">
        <div className="upload-card">
          <div className="card-heading">
            <div>
              <p className="eyebrow">01 / NEW SCAN</p>
              <h2>Scan a product</h2>
            </div>
            <Camera size={23} />
          </div>
          <form onSubmit={handleScan}>
            <label className="dropzone">
              <UploadCloud size={30} />
              <strong>{file ? file.name : "Choose a product image"}</strong>
              <span>JPEG, PNG or WEBP · up to 12 MB</span>
              <input
                type="file"
                accept="image/jpeg,image/png,image/webp"
                onChange={(event) => setFile(event.target.files?.[0] || null)}
              />
            </label>
            <button disabled={busy || !file} type="submit">
              {busy ? "Uploading…" : "Upload for analysis"}
            </button>
          </form>
          {message && <p className="status" role="status">{message}</p>}
          <p className="disclaimer">
            This starter build accepts an image but does not yet run a trained recognition model.
          </p>
        </div>

        <aside className="side-card">
          <div className="side-icon"><PackageSearch size={22} /></div>
          <p className="eyebrow">THE WORKFLOW</p>
          <h2>From label to inventory.</h2>
          <ul>
            <li><span>01</span> Detect product-label information</li>
            <li><span>02</span> Recognise and classify date fields</li>
            <li><span>03</span> Review uncertain readings</li>
            <li><span>04</span> Save verified product records</li>
          </ul>
          <div className="trust-note"><ShieldCheck size={17} /> Uncertain dates should always be verified.</div>
        </aside>
      </section>
      <footer>ExpiryLens · Deep Learning project scaffold · v0.1.0</footer>
    </main>
  );
}
